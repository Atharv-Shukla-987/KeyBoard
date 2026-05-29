# ============================================================
#  keymap.py — 60% Cherry MX layout, 3 layers
#
#  FN_KEY = 0xFF  marker (not a real HID keycode)
#  NO     = None  transparent (fall through to layer below)
#  BLK    = False hard block (sends nothing)
# ============================================================
from adafruit_hid.keycode import Keycode as K

FN_KEY = 0xFF
NO     = None
BLK    = False

#      col: 0          1      2      3       4       5      6       7       8       9      10       11            12        13
BASE = [
    [K.ESCAPE,   K.ONE,  K.TWO,  K.THREE, K.FOUR, K.FIVE, K.SIX,  K.SEVEN,K.EIGHT,K.NINE, K.ZERO, K.MINUS,      K.EQUALS, K.BACKSPACE],
    [K.TAB,      K.Q,    K.W,    K.E,     K.R,    K.T,    K.Y,    K.U,    K.I,    K.O,    K.P,    K.LEFT_BRACKET,K.RIGHT_BRACKET, K.BACKSLASH],
    [K.CAPS_LOCK,K.A,    K.S,    K.D,     K.F,    K.G,    K.H,    K.J,    K.K,    K.L,    K.SEMICOLON, K.QUOTE, NO,       K.RETURN],
    [K.LEFT_SHIFT,K.Z,   K.X,    K.C,     K.V,    K.B,    K.N,    K.M,    K.COMMA,K.PERIOD,K.FORWARD_SLASH, NO, NO,       K.RIGHT_SHIFT],
    [K.LEFT_CONTROL, NO, K.LEFT_ALT, NO,  NO,     K.SPACEBAR, NO, NO,     NO,     K.RIGHT_ALT, NO, FN_KEY,       K.APPLICATION, K.RIGHT_CONTROL],
]

FN = [
    [K.GRAVE_ACCENT,K.F1, K.F2,  K.F3,   K.F4,   K.F5,   K.F6,   K.F7,   K.F8,   K.F9,  K.F10,  K.F11,        K.F12,    K.DELETE],
    [NO,         NO,     NO,     NO,      NO,     NO,     NO,     NO,     NO,     NO,     K.PRINT_SCREEN, K.SCROLL_LOCK, K.PAUSE, NO],
    [NO,         NO,     NO,     NO,      NO,     NO,     NO,     NO,     NO,     NO,     NO,      NO,           NO,       NO],
    [NO,         NO,     NO,     NO,      NO,     NO,     NO,     NO,     NO,     NO,     NO,      NO,           NO,       NO],
    [NO,         NO,     NO,     NO,      NO,     NO,     NO,     NO,     NO,     NO,     NO,      FN_KEY,       NO,       NO],
]

NAV = [
    [NO, NO,   NO,   NO,   NO,   NO,   NO,   NO,       NO,      NO,     NO,          NO,   NO,   NO],
    [NO, NO,   NO,   NO,   NO,   NO,   NO,   K.HOME,   K.UP,    K.END,  K.PAGE_UP,   NO,   NO,   NO],
    [NO, NO,   NO,   NO,   NO,   NO,   NO,   K.LEFT,   K.DOWN,  K.RIGHT,K.PAGE_DOWN, NO,   NO,   NO],
    [NO, NO,   NO,   NO,   NO,   NO,   NO,   NO,       NO,      NO,     NO,          NO,   NO,   NO],
    [NO, NO,   NO,   NO,   NO,   NO,   NO,   NO,       NO,      NO,     NO,          FN_KEY,NO,  NO],
]

LAYERS = [BASE, FN, NAV]

MODIFIER_MAP = {
    K.LEFT_CONTROL:  0x01,
    K.LEFT_SHIFT:    0x02,
    K.LEFT_ALT:      0x04,
    K.LEFT_GUI:      0x08,
    K.RIGHT_CONTROL: 0x10,
    K.RIGHT_SHIFT:   0x20,
    K.RIGHT_ALT:     0x40,
    K.RIGHT_GUI:     0x80,
}
