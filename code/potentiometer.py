# ============================================================
#  potentiometer.py — PTA4543-2010CPB103 linear potentiometer
#
#  Wiring:
#    Left pin  (pin 1) → 3.3V
#    Right pin (pin 3) → GND
#    Wiper     (pin 2) → GP26 (ADC0)
#
#  The PTA4543 is a 10kΩ slide pot with ~20mm travel.
#  Returns 0–100% with a dead-band threshold to suppress noise.
# ============================================================
import analogio
from config import SLIDER_PIN, SLIDER_THRESHOLD


class Potentiometer:
    def __init__(self):
        self._adc  = analogio.AnalogIn(SLIDER_PIN)
        self._last = -999

    @property
    def percentage(self) -> int:
        return int(self._adc.value / 65535 * 100)

    def poll(self):
        """
        Returns (changed: bool, value: int 0–100).
        Only fires when movement exceeds SLIDER_THRESHOLD %.
        """
        pct = self.percentage
        if abs(pct - self._last) >= SLIDER_THRESHOLD:
            self._last = pct
            return True, pct
        return False, self._last
