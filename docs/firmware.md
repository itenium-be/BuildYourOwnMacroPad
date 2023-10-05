# Firmware

## Downloads

- [Mu Editor](https://codewith.mu/en/download) The IDE we'll use to program our macropad
- [CircuitPython runtime](https://circuitpython.org/board/seeeduino_xiao_rp2040/) The CircuitPython runtime for our board
- [CircuitPython Essentials](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases) Grab the latest release here and unzip it on your PC. Make sure you get the `8.x-mpy` version.

## Initial Setup

Follow the [guide](https://wiki.seeedstudio.com/XIAO-RP2040-with-CircuitPython/) here until you can blink the built-in LED. After this you should be able to get new code on your board and run it.

You'll have to reset the board using the two ~tiny~ buttons, then drag the downloaded runtime onto the board (it shows up as an external drive). It should reboot immediately and show up as a drive called `CIRCUITPY`. If this worked, you're ready to open up the Mu editor!

## Installing libraries from CircuitPython essentials

To install some of the libraries we're going to use, drag them into the `lib` folder on the `CIRCUITPY` external drive. You can find them in the CircuitPython Essentials folder you've unzipped previously. We'll need two libraries:

- The `adafruit_hid` folder
- The `neopixel.mpy` file

## Programming the keys

To read all of our key inputs we'll be using the [keypad](https://docs.circuitpython.org/en/latest/shared-bindings/keypad/index.html) built-in library of CircuitPython.

Read [this tutorial](https://learn.adafruit.com/key-pad-matrix-scanning-in-circuitpython/overview) up to the second page, we'll base our code on [their example](https://learn.adafruit.com/key-pad-matrix-scanning-in-circuitpython/keys-one-key-per-pin#macropad-example-3099041). Our keys are set up a bit differently though, so I'll help you with the setup code:

```py
KEY_PINS = (
    board.D1,
    board.D2,
    board.D3,
    board.D4,
    board.D5,
    board.D6,
    board.D7 # Rotary encoder click
)

KEYCODES = (
    Keycode.ONE,
    Keycode.TWO,
    Keycode.THREE,
    Keycode.FOUR,
    Keycode.FIVE,
    Keycode.SIX,
    Keycode.SEVEN
)
```

The built in neopixel is a bit different as well, we only have the one.

```py
neopixel = neopixel.NeoPixel(board.NEOPIXEL, 1, brightness=0.4)
neopixel.fill(OFF_COLOR)
```

And instead of lighting up a specific NeoPixel, we'll always light up our single one. Replace `neopixels[key_number] = ON_COLOR` with `neopixel.fill(ON_COLOR)`.

## Programming the rotary encoder

We'll use the built-in `rotary-encoder` library to read out our knob. Follow [this tutorial](https://learn.adafruit.com/rotary-encoder/circuitpython) to get the rotary encoder running.

## Completed code
