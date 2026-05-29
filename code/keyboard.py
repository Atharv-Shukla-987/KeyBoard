# ============================================================
#  keyboard.py — Cherry MX matrix scanner (5 rows × 14 cols)
#  Diodes: 1N4148, anode toward switch, cathode toward ROW pin
# ============================================================
import time
import digitalio
from config import ROW_PINS, COL_PINS


class MatrixScanner:
    def __init__(self):
        self.rows = []
        for pin in ROW_PINS:
            r = digitalio.DigitalInOut(pin)
            r.direction = digitalio.Direction.OUTPUT
            r.value = False
            self.rows.append(r)

        self.cols = []
        for pin in COL_PINS:
            c = digitalio.DigitalInOut(pin)
            c.direction = digitalio.Direction.INPUT
            c.pull = digitalio.Pull.DOWN
            self.cols.append(c)

        self._prev: set = set()

    def scan(self):
        """
        Returns (held, newly_pressed, newly_released) as sets of (row, col).
        """
        held = set()
        for ri, row in enumerate(self.rows):
            row.value = True
            time.sleep(0.000005)
            for ci, col in enumerate(self.cols):
                if col.value:
                    held.add((ri, ci))
            row.value = False

        pressed  = held - self._prev
        released = self._prev - held
        self._prev = held
        return held, pressed, released
