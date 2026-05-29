# ============================================================
#  battery.py — LiPo battery monitor
#
#  Circuit:
#    LiPo (+) ──┬── 100kΩ ── GP27 (ADC1) ── 100kΩ ── GND
#               └── MCP1700 ── 3.3V rail (powers everything)
#
#  The TP4056 charges the LiPo via the USB-C charging port.
#  We read the raw LiPo voltage through a 1:1 divider so the
#  ADC sees max ~2.1V (4.2V / 2) which is safe for the Pico.
# ============================================================
import analogio
from config import (BATTERY_PIN, BATTERY_FULL_V,
                    BATTERY_EMPTY_V, BATTERY_DIVIDER)

# Pico ADC reference = 3.3V, 16-bit
_ADC_REF  = 3.3
_ADC_BITS = 65535


class Battery:
    def __init__(self):
        self._adc      = analogio.AnalogIn(BATTERY_PIN)
        self._percent  = 100
        self.update()

    def update(self):
        """Read voltage and recalculate percentage."""
        raw     = self._adc.value
        v_adc   = (raw / _ADC_BITS) * _ADC_REF
        v_batt  = v_adc * BATTERY_DIVIDER            # un-divide

        span    = BATTERY_FULL_V - BATTERY_EMPTY_V
        above   = v_batt - BATTERY_EMPTY_V
        pct     = int(max(0, min(100, (above / span) * 100)))
        self._percent = pct
        return pct

    @property
    def percentage(self) -> int:
        return self._percent

    @property
    def is_low(self) -> bool:
        return self._percent <= 15

    @property
    def is_critical(self) -> bool:
        return self._percent <= 5
