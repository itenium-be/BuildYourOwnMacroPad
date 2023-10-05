# Software setup

In this section we'll set up the software we need for this project, and we'll make the built-in LED blink. The hardware equivalent of `Hello world!`.

## Downloads

- [Mu Editor](https://codewith.mu/en/download) The IDE we'll use to program our macropad
- [CircuitPython runtime](https://circuitpython.org/board/seeeduino_xiao_rp2040/) The CircuitPython runtime for our board
- [CircuitPython Essentials](https://github.com/adafruit/Adafruit_CircuitPython_Bundle/releases) Grab the latest release here and unzip it on your PC. Make sure you get the `8.x-mpy` version.

## Initial Setup

Follow the [guide](https://wiki.seeedstudio.com/XIAO-RP2040-with-CircuitPython/) here until you can blink the built-in LED. After this you should be able to get new code on your board and run it.

You'll have to reset the board using the two ~tiny~ buttons, then drag the downloaded runtime onto the board (it shows up as an external drive). It should reboot immediately and show up as a drive called `CIRCUITPY`. If this worked, you're ready to open up the Mu editor!

Try to run the code from the tutorial, and hopefully, watch the blinking lights!

## Installing libraries from CircuitPython essentials

To install some of the libraries we're going to use, drag them into the `lib` folder on the `CIRCUITPY` external drive. You can find them in the CircuitPython Essentials folder you've unzipped previously. We'll need two libraries:

- The `adafruit_hid` folder
- The `neopixel.mpy` file

**Next up** Wiring and programming the [rotary encoder](rotary-encoder.md)!
