# ============================================================
#  config.py — Hardware config for Atharv's 60% Keyboard
#
#  MCU         : Raspberry Pi Pico W
#  Switches    : Cherry MX
#  Display     : SSD1306 0.96" 128×64 I2C
#  Slider      : PTA4543-2010CPB103 linear potentiometer
#  LEDs        : SK6812 MINI (underglow)
#  Battery     : 3.7V 2000mAh LiPo
#  Charger     : TP4056 (USB-C charging port)
#  Regulator   : MCP1700 (3.3V from LiPo)
#  Mode switch : Physical SLIDE SWITCH (not push button)
#  Dongle      : ESP32-S3 Mini + USB Type-A → USB HID
# ============================================================
import board

# ── Matrix (Cherry MX, 1N4148 diodes in ROW direction) ──────
ROW_PINS = [board.GP0, board.GP1, board.GP2, board.GP3, board.GP4]
COL_PINS = [
    board.GP5,  board.GP6,  board.GP7,  board.GP8,
    board.GP9,  board.GP10, board.GP11, board.GP12,
    board.GP13, board.GP14, board.GP15, board.GP16,
    board.GP17, board.GP18,
]

# ── OLED (SSD1306 I2C, 128×64) ──────────────────────────────
OLED_SDA    = board.GP20
OLED_SCL    = board.GP21
OLED_ADDR   = 0x3C
OLED_WIDTH  = 128
OLED_HEIGHT = 64

# ── PTA4543 Linear Potentiometer (ADC) ──────────────────────
# PTA4543-2010CPB103 = 10kΩ travel ~20mm
SLIDER_PIN        = board.GP26   # ADC0 — wiper pin
SLIDER_THRESHOLD  = 2            # % dead-band to avoid noise

# ── Battery ADC (voltage divider on LiPo cell) ──────────────
# Use a 100kΩ / 100kΩ divider: VBAT → 100k → GP27 → 100k → GND
# Gives VBAT/2 at ADC, readable by Pico (max 3.3V on ADC)
BATTERY_PIN       = board.GP27   # ADC1
BATTERY_FULL_V    = 4.2          # LiPo full voltage
BATTERY_EMPTY_V   = 3.0          # LiPo cutoff voltage
BATTERY_DIVIDER   = 2.0          # resistor divider ratio (1:1 = ×2)

# ── SK6812 MINI Underglow ────────────────────────────────────
LED_PIN        = board.GP28
LED_COUNT      = 10              # adjust to actual strip length
LED_BRIGHTNESS = 0.25            # keep low on battery power

# ── Mode Slide Switch ────────────────────────────────────────
# SLIDE SWITCH: one pin reads HIGH=USB, LOW=Dongle
# Wire: centre pin → GP22, one side → 3.3V, other side → GND
MODE_SWITCH_PIN = board.GP22

# ── UART to ESP32-S3 (dongle mode) ──────────────────────────
# Note: GP0/GP1 are also ROW0/ROW1. If your PCB uses separate
# UART traces, change these to free GPIOs (e.g. GP8/GP9).
UART_TX   = board.GP8
UART_RX   = board.GP9
UART_BAUD = 115200

# ── Timing ──────────────────────────────────────────────────
OLED_REFRESH_HZ    = 10
LED_REFRESH_HZ     = 30
BATTERY_CHECK_SEC  = 30.0        # how often to re-read battery
DONGLE_KEEPALIVE_S = 5.0

# ── Layer names ─────────────────────────────────────────────
LAYER_NAMES = ["Base", "Fn", "Nav"]
