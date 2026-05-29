# ============================================================
#  leds.py — SK6812 MINI underglow controller
#
#  SK6812 MINI uses GRBW protocol (4 channels).
#  On battery: auto-dims when charge drops below 20%.
#
#  Effects (cycle with FN + [ / ]):
#    0  Static
#    1  Breathing
#    2  Rainbow wave
#    3  Layer colour  (colour changes per active layer)
#    4  Reactive flash (lights up on keypress, fades out)
#    5  Off
# ============================================================
import time
import math
import neopixel
from config import LED_PIN, LED_COUNT, LED_BRIGHTNESS

BLACK  = (0,   0,   0)
CYAN   = (0,   180, 180)
PURPLE = (130, 0,   180)
GREEN  = (0,   180, 0)
WHITE  = (200, 200, 200)
ORANGE = (220, 80,  0)

LAYER_COLOURS = [CYAN, PURPLE, GREEN]   # Base, Fn, Nav
EFFECT_NAMES  = ["Static", "Breathe", "Rainbow", "Layer", "Reactive", "Off"]
NUM_EFFECTS   = len(EFFECT_NAMES)


class LEDController:
    def __init__(self):
        self._px = neopixel.NeoPixel(
            LED_PIN, LED_COUNT,
            brightness=LED_BRIGHTNESS,
            auto_write=False,
            pixel_order=neopixel.GRBW   # SK6812 MINI
        )
        self._effect      = 0
        self._layer       = 0
        self._t           = 0.0
        self._hue         = 0.0
        self._static_col  = CYAN
        self._reactive_t  = -999.0
        self._battery_pct = 100

    # ── Public API ───────────────────────────────────────────

    @property
    def effect_name(self) -> str:
        return EFFECT_NAMES[self._effect]

    def set_effect(self, index: int):
        self._effect = index % NUM_EFFECTS

    def next_effect(self):
        self.set_effect(self._effect + 1)

    def prev_effect(self):
        self.set_effect(self._effect - 1)

    def set_layer(self, layer: int):
        self._layer = layer

    def set_battery(self, pct: int):
        """Pass battery % so LEDs auto-dim when low."""
        self._battery_pct = pct

    def notify_keypress(self):
        self._reactive_t = time.monotonic()

    def tick(self, delta: float):
        self._t += delta

        # Auto-dim on low battery to save power
        if self._battery_pct <= 20:
            self._px.brightness = LED_BRIGHTNESS * (self._battery_pct / 20) * 0.5
        else:
            self._px.brightness = LED_BRIGHTNESS

        {
            0: self._fx_static,
            1: self._fx_breathe,
            2: self._fx_rainbow,
            3: self._fx_layer,
            4: self._fx_reactive,
            5: self._fx_off,
        }.get(self._effect, self._fx_off)()

        self._px.show()

    # ── Effects ──────────────────────────────────────────────

    def _fill(self, r, g, b, scale=1.0):
        s = max(0.0, min(1.0, scale))
        colour = (int(r*s), int(g*s), int(b*s), 0)
        for i in range(LED_COUNT):
            self._px[i] = colour

    def _fx_static(self):
        r, g, b = self._static_col
        self._fill(r, g, b)

    def _fx_breathe(self):
        bright = (math.sin(self._t * 2.1) + 1.0) / 2.0
        r, g, b = self._static_col
        self._fill(r, g, b, bright)

    def _fx_rainbow(self):
        self._hue = (self._hue + 0.6) % 360
        for i in range(LED_COUNT):
            hue = (self._hue + i * (360 / LED_COUNT)) % 360
            self._px[i] = self._hsv(hue) + (0,)

    def _fx_layer(self):
        r, g, b = LAYER_COLOURS[self._layer % len(LAYER_COLOURS)]
        self._fill(r, g, b)

    def _fx_reactive(self):
        age = time.monotonic() - self._reactive_t
        FADE = 0.35
        if age < FADE:
            self._fill(255, 255, 255, 1.0 - age / FADE)
        else:
            self._fx_off()

    def _fx_off(self):
        self._fill(0, 0, 0)

    # ── HSV helper ───────────────────────────────────────────
    @staticmethod
    def _hsv(hue: float) -> tuple:
        h = hue / 60.0
        i = int(h)
        f = h - i
        q, t, v = int(255*(1-f)), int(255*f), 255
        return [(v,t,0),(q,v,0),(0,v,t),(0,q,v),(t,0,v),(v,0,q)][i % 6]
