# ============================================================
#  hid_devices.py — Unified HID output
#
#  USB mode   : Pico W USB-C → host, acts as USB HID keyboard
#  Dongle mode: Pico W UART → ESP32-S3 → USB-A → host as HID
#
#  The mode is read from a PHYSICAL SLIDE SWITCH on GP22.
#  No software toggle needed — just flip the switch.
# ============================================================
import json
import digitalio
import busio
import usb_hid

from adafruit_hid.keyboard           import Keyboard
from adafruit_hid.consumer_control   import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

from config  import MODE_SWITCH_PIN, UART_TX, UART_RX, UART_BAUD
from keymap  import MODIFIER_MAP


# ── Slide switch reader ──────────────────────────────────────
class ModeSwitch:
    """
    Reads the physical slide switch.
    HIGH = USB mode (Pico USB-C to host)
    LOW  = Dongle mode (via ESP32-S3 USB-A dongle)
    """
    def __init__(self):
        self._pin = digitalio.DigitalInOut(MODE_SWITCH_PIN)
        self._pin.direction = digitalio.Direction.INPUT
        self._pin.pull = digitalio.Pull.DOWN

    @property
    def mode(self) -> str:
        return "USB" if self._pin.value else "Dongle"

    def changed(self, prev: str) -> bool:
        return self.mode != prev


# ── USB HID backend ──────────────────────────────────────────
class UsbHid:
    def __init__(self):
        self._kbd  = Keyboard(usb_hid.devices)
        self._cc   = ConsumerControl(usb_hid.devices)
        self._held: set = set()

    def press(self, keycode: int):
        if keycode in self._held:
            return
        self._held.add(keycode)
        try:
            self._kbd.press(keycode)
        except Exception:
            pass

    def release(self, keycode: int):
        self._held.discard(keycode)
        try:
            self._kbd.release(keycode)
        except Exception:
            pass

    def release_all(self):
        self._held.clear()
        self._kbd.release_all()

    def volume_step(self, up: bool):
        code = (ConsumerControlCode.VOLUME_INCREMENT if up
                else ConsumerControlCode.VOLUME_DECREMENT)
        self._cc.press(code)
        self._cc.release()

    def slider(self, pct: int):
        pass   # volume_step handles it via main.py direction tracking


# ── UART → ESP32-S3 dongle backend ───────────────────────────
class DongleHid:
    """
    Sends newline-delimited JSON to ESP32-S3 over UART.
    ESP32-S3 enumerates as USB HID keyboard toward the host PC
    via its USB Type-A connector (D+/D- connected to host).

    Packet types:
      {"t":"k","m":<mod>,"k":[kc,...]}  key report
      {"t":"r"}                          release all
      {"t":"s","v":<0-100>}              slider / volume
      {"t":"p"}                          keepalive ping
    """
    def __init__(self):
        self._uart     = busio.UART(UART_TX, UART_RX, baudrate=UART_BAUD)
        self._held_mod = 0
        self._held_kc: list = []

    def _send(self, obj: dict):
        try:
            self._uart.write((json.dumps(obj) + "\n").encode())
        except Exception as e:
            print(f"[UART] {e}")

    def press(self, keycode: int):
        if keycode in MODIFIER_MAP:
            self._held_mod |= MODIFIER_MAP[keycode]
        else:
            if keycode not in self._held_kc:
                self._held_kc.append(keycode)
        self._flush()

    def release(self, keycode: int):
        if keycode in MODIFIER_MAP:
            self._held_mod &= ~MODIFIER_MAP[keycode]
        else:
            if keycode in self._held_kc:
                self._held_kc.remove(keycode)
        self._flush()

    def release_all(self):
        self._held_mod = 0
        self._held_kc  = []
        self._send({"t": "r"})

    def _flush(self):
        self._send({"t": "k", "m": self._held_mod,
                    "k": self._held_kc[:6]})

    def slider(self, pct: int):
        self._send({"t": "s", "v": pct})

    def volume_step(self, up: bool):
        pass   # handled by ESP32 from slider packets

    def ping(self):
        self._send({"t": "p"})


# ── Unified HID device ────────────────────────────────────────
class HIDDevice:
    """
    Wraps both backends. Mode is determined by the slide switch.
    Call refresh_mode() each loop iteration to detect switch flips.
    """
    def __init__(self):
        self._switch  = ModeSwitch()
        self._usb     = UsbHid()
        self._dongle  = None   # lazy-init (UART alloc)
        self._mode    = self._switch.mode
        self._backend = self._usb if self._mode == "USB" else self._get_dongle()

    def _get_dongle(self) -> DongleHid:
        if self._dongle is None:
            self._dongle = DongleHid()
        return self._dongle

    def refresh_mode(self) -> bool:
        """
        Checks slide switch. If mode changed, switches backend.
        Returns True if a switch flip was detected.
        """
        new_mode = self._switch.mode
        if new_mode != self._mode:
            self._backend.release_all()
            self._mode = new_mode
            self._backend = (self._usb if new_mode == "USB"
                             else self._get_dongle())
            print(f"[HID] Mode → {new_mode}")
            return True
        return False

    @property
    def mode(self) -> str:
        return self._mode

    def press(self, keycode: int):
        self._backend.press(keycode)

    def release(self, keycode: int):
        self._backend.release(keycode)

    def release_all(self):
        self._backend.release_all()

    def slider(self, pct: int):
        self._backend.slider(pct)

    def volume_step(self, up: bool):
        self._backend.volume_step(up)

    def ping(self):
        if self._mode == "Dongle" and self._dongle:
            self._dongle.ping()
