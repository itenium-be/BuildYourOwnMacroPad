import rotaryio
import board
import keypad
import neopixel
import usb_hid
from adafruit_hid.keyboard import Keyboard
from adafruit_hid.keycode import Keycode
from adafruit_hid.consumer_control import ConsumerControl
from adafruit_hid.consumer_control_code import ConsumerControlCode

encoder = rotaryio.IncrementalEncoder(board.D9, board.D10)

cc = ConsumerControl(usb_hid.devices)

button_state = None
last_position = encoder.position

KEY_PINS = (
    board.D1,
    board.D2,
    board.D3,
    board.D4,
    board.D5,
    board.D6,
    board.D7,  # Rotary encoder click
)

KEYCODES = (
    [Keycode.WINDOWS, Keycode.E], # Open explorer
    [Keycode.WINDOWS, Keycode.M], # Minimize all windows
    [Keycode.WINDOWS, Keycode.L], # Lock your PC
    [Keycode.F13], # Assignable in AutoHotKey
    [Keycode.F14], # Assignable in AutoHotKey
    [Keycode.F15], # Assignable in AutoHotKey
    [Keycode.WINDOWS, Keycode.SHIFT, Keycode.A],  # PowerToys mute/unmute
)

ON_COLOR = (0, 0, 255)
OFF_COLOR = (0, 20, 0)

keys = keypad.Keys(KEY_PINS, value_when_pressed=False, pull=True)
neopixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.4)
neopixel.fill(OFF_COLOR)
kbd = Keyboard(usb_hid.devices)

while True:
    event = keys.events.get()
    if event:
        key_number = event.key_number
        # A key transition occurred.
        if event.pressed:
            kbd.send(*KEYCODES[key_number])
            neopixel.fill(ON_COLOR)

        if event.released:
            neopixel.fill(OFF_COLOR)

    current_position = encoder.position
    position_change = current_position - last_position
    if position_change > 0:
        for _ in range(position_change):
            cc.send(ConsumerControlCode.VOLUME_INCREMENT)
    elif position_change < 0:
        for _ in range(-position_change):
            cc.send(ConsumerControlCode.VOLUME_DECREMENT)
    last_position = current_position
