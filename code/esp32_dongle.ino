/*
 * ============================================================
 *  esp32_dongle.ino — ESP32-S3 Mini USB HID Dongle
 *  github.com/Atharv-Shukla-987/KeyBoard
 *
 *  Architecture:
 *    Pico W ──UART──► ESP32-S3 ──USB-A──► Host PC
 *
 *  The ESP32-S3 enumerates as a USB HID keyboard toward the
 *  host via its USB Type-A connector (D+ and D- connected).
 *  Key reports arrive as JSON over UART from the Pico W.
 *
 *  Wiring:
 *    ESP32-S3 GPIO17 (RX) ← Pico W TX  (3.3V logic, shared GND)
 *    ESP32-S3 GPIO18 (TX) → Pico W RX
 *    USB Type-A pin 2 (D−) → ESP32-S3 USB D−
 *    USB Type-A pin 3 (D+) → ESP32-S3 USB D+
 *    USB Type-A pin 1 (VBUS 5V) → MCP1700 in → regulated 3.3V
 *    USB Type-A pin 4 (GND) → GND
 *
 *  Board  : ESP32S3 Dev Module
 *  USB Mode: "USB-OTG (TinyUSB)"  ← set in Arduino IDE Tools menu
 *  Library: ArduinoJson v6 (Library Manager)
 *           USB built-in (ESP32 Arduino core ≥ 2.0.5)
 * ============================================================
 */

#include <Arduino.h>
#include <USB.h>
#include <USBHIDKeyboard.h>
#include <USBHIDConsumerControl.h>
#include <ArduinoJson.h>

// ── UART from Pico W ─────────────────────────────────────────
#define PICO_RX_PIN  17
#define PICO_TX_PIN  18
#define UART_BAUD    115200

// ── Status LED (onboard) ─────────────────────────────────────
#define LED_PIN 2

HardwareSerial     PicoUART(1);
USBHIDKeyboard     Keyboard;
USBHIDConsumerControl Consumer;

// ── Volume state (for slider → volume mapping) ───────────────
int lastVolLevel = -1;

// ── UART receive buffer ──────────────────────────────────────
String uartBuf = "";

// ── Send a full keyboard HID report ─────────────────────────
void sendKeyReport(uint8_t modifier, uint8_t* keys, uint8_t count) {
    // Release previous, then press new keys
    Keyboard.releaseAll();

    // Press modifier keys
    if (modifier & 0x01) Keyboard.press(KEY_LEFT_CTRL);
    if (modifier & 0x02) Keyboard.press(KEY_LEFT_SHIFT);
    if (modifier & 0x04) Keyboard.press(KEY_LEFT_ALT);
    if (modifier & 0x08) Keyboard.press(KEY_LEFT_GUI);
    if (modifier & 0x10) Keyboard.press(KEY_RIGHT_CTRL);
    if (modifier & 0x20) Keyboard.press(KEY_RIGHT_SHIFT);
    if (modifier & 0x40) Keyboard.press(KEY_RIGHT_ALT);
    if (modifier & 0x80) Keyboard.press(KEY_RIGHT_GUI);

    // Press keycodes (CircuitPython Keycode values match USB HID directly)
    for (uint8_t i = 0; i < min(count, (uint8_t)6); i++) {
        if (keys[i] > 0) Keyboard.press(keys[i]);
    }
}

void releaseAll() {
    Keyboard.releaseAll();
}

// ── Slider → volume (direction-based) ────────────────────────
void handleSlider(int pct) {
    int level = pct / 7;   // 0–14 steps
    if (level == lastVolLevel) return;

    bool up = (level > lastVolLevel);
    int  steps = abs(level - lastVolLevel);
    lastVolLevel = level;

    for (int i = 0; i < steps; i++) {
        Consumer.press(up ? CONSUMER_VOLUME_INCREMENT
                         : CONSUMER_VOLUME_DECREMENT);
        Consumer.release();
        delay(8);
    }
}

// ── Parse UART JSON packet ────────────────────────────────────
void processPacket(const String& line) {
    StaticJsonDocument<128> doc;
    if (deserializeJson(doc, line) != DeserializationError::Ok) {
        Serial.println("[JSON] parse error: " + line);
        return;
    }

    const char* t = doc["t"];
    if (!t) return;

    if (strcmp(t, "k") == 0) {
        // Key report
        uint8_t mod = doc["m"] | 0;
        JsonArray arr = doc["k"];
        uint8_t keys[6] = {0};
        uint8_t n = 0;
        for (uint8_t kc : arr) {
            if (n >= 6) break;
            keys[n++] = kc;
        }
        if (n == 0 && mod == 0) {
            releaseAll();
        } else {
            sendKeyReport(mod, keys, n);
        }

    } else if (strcmp(t, "r") == 0) {
        // Explicit release all
        releaseAll();

    } else if (strcmp(t, "s") == 0) {
        // Slider / volume
        int v = doc["v"] | 0;
        handleSlider(v);

    } else if (strcmp(t, "p") == 0) {
        // Keepalive ping — ACK back
        PicoUART.println("{\"t\":\"ok\"}");
    }
}

// ── Setup ────────────────────────────────────────────────────
void setup() {
    Serial.begin(115200);
    pinMode(LED_PIN, OUTPUT);
    digitalWrite(LED_PIN, LOW);

    // UART from Pico W
    PicoUART.begin(UART_BAUD, SERIAL_8N1, PICO_RX_PIN, PICO_TX_PIN);
    Serial.printf("[UART] RX=%d TX=%d @ %d baud\n",
                  PICO_RX_PIN, PICO_TX_PIN, UART_BAUD);

    // USB HID — enumerates toward host via USB Type-A D+/D-
    USB.manufacturerName("Atharv");
    USB.productName("mech_board dongle");
    USB.begin();
    Keyboard.begin();
    Consumer.begin();

    digitalWrite(LED_PIN, HIGH);   // solid = USB enumerated
    Serial.println("[USB] HID keyboard dongle ready");
}

// ── Loop ─────────────────────────────────────────────────────
void loop() {
    while (PicoUART.available()) {
        char c = PicoUART.read();
        if (c == '\n') {
            uartBuf.trim();
            if (uartBuf.length() > 0) {
                processPacket(uartBuf);
            }
            uartBuf = "";
        } else {
            uartBuf += c;
        }
    }
}
