# Give me the code!

## Setting up CircuitPython

Follow [this guide](https://wiki.seeedstudio.com/XIAO-RP2040-with-CircuitPython/) to flash the latest CircuitPython release on your microcontroller, ask for help if something doesn't work from the first try.

```py
import time
import board
import digitalio
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.keyboard_layout_us import KeyboardLayoutUS
from adafruit_hid.consumer_control_code import ConsumerControlCode
from pico_macropad.encoder import Encoder
from pico_macropad.hid import ConsumerCtrl
import keypad
import neopixel

# Setup NeoPixel
neopixels = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.3)
ON_COLOR = (0, 0, 255)
OFF_COLOR = (0, 20, 0)
neopixels[0] = OFF_COLOR
neopixels.show()

# Setup rotary encoder
encoder_cw_key = ConsumerCtrl(ConsumerControlCode.VOLUME_INCREMENT)
encoder_ccw_key = ConsumerCtrl(ConsumerControlCode.VOLUME_DECREMENT)
encoder_btn_key = ConsumerCtrl(ConsumerControlCode.MUTE)
encoder = Encoder(board.D9, board.D10, board.D7, 2)

# Setup keys
KEY_PINS = [board.D1, board.D2, board.D3, board.D4, board.D5, board.D6]
KEYCODES = [Keycode.ONE, Keycode.TWO, Keycode.THREE, Keycode.FOUR, Keycode.FIVE, Keycode.SIX]

keys = keypad.Keys(KEY_PINS, value_when_pressed=False, pull=True)
time.sleep(1)
kbd = Keyboard(usb_hid.devices)
keyboard_layout = KeyboardLayoutUS(kbd)

# Main loop
while True:
    event = keys.events.get()
    if event:
        key_number = event.key_number
        if event.pressed:
            kbd.press(KEYCODES[key_number])
            neopixels[0] = ON_COLOR

        if event.released:
            kbd.release(KEYCODES[key_number])
            neopixels[0] = OFF_COLOR

    event = encoder.getButtonEvent()
    if event:
        if event.pressed:
            encoder_btn_key.press()
            neopixels[0] = ON_COLOR
        else:
            encoder_btn_key.release()
            neopixels[0] = OFF_COLOR

    event = encoder.getPositionEvent()
    if event:
        key = encoder_cw_key if event.difference > 0 else encoder_ccw_key
        for x in range(abs(event.difference)):
            key.send()

```
