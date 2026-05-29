# ============================================================
#  boot.py — Runs before main.py, before USB enumerates.
#  Enables USB HID for USB mode operation.
# ============================================================
import usb_hid
import storage

usb_hid.enable((
    usb_hid.Device.KEYBOARD,
    usb_hid.Device.CONSUMER_CONTROL,
    usb_hid.Device.MOUSE,
))

# Keep CIRCUITPY writable from Pico side for editing files
# Comment this out to allow editing from host PC instead
storage.disable_usb_drive()
