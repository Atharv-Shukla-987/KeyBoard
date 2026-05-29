# ============================================================
#  display.py — SSD1306 0.96" OLED (128×64 I2C)
#
#  Primary purpose per README: show battery percentage.
#  Also shows: mode (USB/Dongle), layer, slider position,
#  low-battery warning, and current LED effect.
# ============================================================
import busio
import adafruit_ssd1306
from config import OLED_SDA, OLED_SCL, OLED_ADDR, OLED_WIDTH, OLED_HEIGHT


class Display:
    """
    Layout:
    ┌──────────────────────────────┐
    │ [USB ]  Base       [CAP]    │  ← mode, layer, caps
    ├──────────────────────────────┤
    │ ████████████░░░░  BATT      │  ← battery bar
    │      78%                    │  ← battery %
    ├──────────────────────────────┤
    │ Vol [███████░░░]  54%       │  ← PTA4543 slider
    │ LED: Rainbow                │  ← LED effect
    └──────────────────────────────┘
    """

    def __init__(self):
        i2c = busio.I2C(OLED_SCL, OLED_SDA)
        self._d = adafruit_ssd1306.SSD1306_I2C(
            OLED_WIDTH, OLED_HEIGHT, i2c, addr=OLED_ADDR
        )
        self.clear()
        self.show()

    def clear(self):
        self._d.fill(0)

    def show(self):
        self._d.show()

    def _text(self, msg, x, y, c=1):
        self._d.text(str(msg), x, y, c)

    def _hline(self, x, y, w):
        self._d.hline(x, y, w, 1)

    def _fill_rect(self, x, y, w, h, c=1):
        self._d.fill_rect(x, y, w, h, c)

    def _rect(self, x, y, w, h, c=1):
        self._d.rect(x, y, w, h, c)

    # ── Splash ────────────────────────────────────────────────
    def splash(self):
        self.clear()
        self._text("  mech_board", 4, 10)
        self._text(" by Atharv", 4, 24)
        self._hline(0, 36, OLED_WIDTH)
        self._text("   Starting...", 4, 44)
        self.show()

    # ── Mode-switch notification ──────────────────────────────
    def notify(self, line1: str, line2: str = ""):
        self.clear()
        self._text(line1, 4, 18)
        if line2:
            self._text(line2, 4, 34)
        self.show()

    # ── Low battery warning ───────────────────────────────────
    def low_battery_warning(self, pct: int):
        self.clear()
        self._text("!! LOW BATTERY !", 0, 10)
        self._text(f"    {pct}% remaining", 0, 28)
        self._text("Please charge!", 4, 46)
        self.show()

    # ── Main HUD ──────────────────────────────────────────────
    def update(self, mode: str, layer: str, battery_pct: int,
               slider_pct: int, caps: bool, led_effect: str):
        self.clear()

        # ── Row 0: Mode badge + layer + CAPS ─────────────────
        badge = f" {mode} "
        bw = len(badge) * 6 + 2
        self._fill_rect(0, 0, bw, 11)
        self._text(badge, 2, 2, 0)
        self._text(layer, bw + 4, 2)
        if caps:
            self._fill_rect(108, 0, 20, 11)
            self._text("CAP", 110, 2, 0)

        self._hline(0, 12, OLED_WIDTH)

        # ── Battery (primary display purpose) ────────────────
        self._text("BATT", 90, 16)
        BAR_X, BAR_Y, BAR_W, BAR_H = 2, 15, 82, 10
        self._rect(BAR_X, BAR_Y, BAR_W, BAR_H)
        filled = int(battery_pct / 100 * (BAR_W - 2))
        if filled > 0:
            # Flash red zone when < 20%
            col = 1
            self._fill_rect(BAR_X + 1, BAR_Y + 1, filled, BAR_H - 2, col)

        # Battery % large text
        self._text(f"{battery_pct:3d}%", 46, 27)

        # Low battery indicator
        if battery_pct <= 15:
            self._text("LOW!", 92, 27)

        self._hline(0, 38, OLED_WIDTH)

        # ── Slider (PTA4543) ──────────────────────────────────
        self._text("Vol", 2, 43)
        SL_X, SL_Y, SL_W, SL_H = 24, 42, 66, 8
        self._rect(SL_X, SL_Y, SL_W, SL_H)
        sl_fill = int(slider_pct / 100 * (SL_W - 2))
        if sl_fill > 0:
            self._fill_rect(SL_X + 1, SL_Y + 1, sl_fill, SL_H - 2)
        self._text(f"{slider_pct:3d}%", 94, 43)

        # ── LED effect name ───────────────────────────────────
        self._text(f"LED:{led_effect[:9]}", 2, 54)

        self.show()
