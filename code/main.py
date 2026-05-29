# ============================================================
#  main.py — mech_board orchestrator (Raspberry Pi Pico W)
#  github.com/Atharv-Shukla-987/KeyBoard
# ============================================================
import time

from config       import (OLED_REFRESH_HZ, LED_REFRESH_HZ,
                           BATTERY_CHECK_SEC, DONGLE_KEEPALIVE_S,
                           LAYER_NAMES)
from keymap       import LAYERS, FN_KEY, MODIFIER_MAP
from keyboard     import MatrixScanner
from potentiometer import Potentiometer
from battery      import Battery
from display      import Display
from leds         import LEDController
from hid_devices  import HIDDevice

from adafruit_hid.keycode import Keycode as K


def resolve(row: int, col: int, layer: int):
    """Walk layer stack with None = transparent."""
    for li in (layer, 0):
        try:
            kc = LAYERS[li][row][col]
        except IndexError:
            continue
        if kc is not None:
            return kc
    return None


def run():
    display = Display()
    display.splash()
    time.sleep(1.5)

    matrix  = MatrixScanner()
    slider  = Potentiometer()
    battery = Battery()
    leds    = LEDController()
    hid     = HIDDevice()

    # State
    layer       = 0
    fn_held     = False
    caps_on     = False
    slider_pct  = slider.percentage
    last_vol_lv = slider_pct // 7

    # Timers
    oled_i   = 1.0 / OLED_REFRESH_HZ
    led_i    = 1.0 / LED_REFRESH_HZ
    oled_t   = 0.0
    led_t    = 0.0
    batt_t   = 0.0
    ping_t   = 0.0
    last_t   = time.monotonic()

    # Initial battery read
    battery.update()
    leds.set_battery(battery.percentage)

    print(f"[KB] Ready — {hid.mode} mode")

    while True:
        now   = time.monotonic()
        delta = now - last_t
        last_t = now

        # ── Slide switch mode check ───────────────────────────
        if hid.refresh_mode():
            label = f"Mode: {hid.mode}"
            display.notify(label)
            time.sleep(0.4)

        # ── Matrix scan ───────────────────────────────────────
        _, pressed, released = matrix.scan()

        for r, c in pressed:
            kc = resolve(r, c, layer)
            if kc is None or kc is False:
                continue

            if kc == FN_KEY:
                fn_held = True
                layer   = 1
                continue

            # FN + [ / ] to cycle LED effects
            if fn_held and kc == K.RIGHT_BRACKET:
                leds.next_effect()
                continue
            if fn_held and kc == K.LEFT_BRACKET:
                leds.prev_effect()
                continue

            if kc == K.CAPS_LOCK:
                caps_on = not caps_on

            leds.notify_keypress()
            hid.press(kc)

        for r, c in released:
            kc = resolve(r, c, layer)
            if kc is None or kc is False:
                continue

            if kc == FN_KEY:
                fn_held = False
                layer   = 0
                continue

            hid.release(kc)

        # ── PTA4543 slider ────────────────────────────────────
        changed, pct = slider.poll()
        if changed:
            slider_pct = pct
            hid.slider(pct)
            # Volume step for USB mode (direction-based)
            lv = pct // 7
            if lv != last_vol_lv:
                hid.volume_step(lv > last_vol_lv)
                last_vol_lv = lv

        # ── Battery check ─────────────────────────────────────
        if now - batt_t >= BATTERY_CHECK_SEC:
            batt_t = now
            battery.update()
            leds.set_battery(battery.percentage)
            if battery.is_critical:
                # Flash warning on OLED, pause LEDs
                display.low_battery_warning(battery.percentage)
                time.sleep(2.0)

        # ── LED tick ─────────────────────────────────────────
        if now >= led_t:
            led_t = now + led_i
            leds.set_layer(layer)
            leds.tick(delta)

        # ── OLED refresh ─────────────────────────────────────
        if now >= oled_t:
            oled_t = now + oled_i
            display.update(
                mode        = hid.mode,
                layer       = LAYER_NAMES[layer],
                battery_pct = battery.percentage,
                slider_pct  = slider_pct,
                caps        = caps_on,
                led_effect  = leds.effect_name,
            )

        # ── Dongle keepalive ──────────────────────────────────
        if hid.mode == "Dongle" and now - ping_t >= DONGLE_KEEPALIVE_S:
            ping_t = now
            hid.ping()

        time.sleep(0.001)


run()
