# DEPRECATED LIBRARY Adafruit Python MAX9744

This library has been deprecated!

We are now only using our CircuitPython sensor libraries in Python.

We are leaving the code up for historical/research purposes but archiving the
repository.

Check out this guide for using the MAX9744 with Python!

https://learn.adafruit.com/adafruit-20w-stereo-audio-amplifier-class-d-max9744/python-circuitpython

----

Python library for controlling the MAX9744 class D amplifier with I2C volume
control on a Raspberry Pi or BeagleBone Black.  Made to work with Adafruit's
MAX9744 20-watt stereo amplifier board: https://www.adafruit.com/product/1752

## Wiring

Connect the MAX9744 board to your hardware's I2C bus as follows:

On a Raspberry Pi connect:
*   Pi 3.3V power to MAX9744 Vi2c pin.
*   Pi GND to MAX9744 GND pin.
*   Pi SCL to MAX9744 SCL pin.
*   Pi SDA to MAX9744 SDA pin.

Additionally make sure you've enabled I2C on your Raspberry Pi, see:
https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

On a BeagleBone Black connect:
*   BeagleBone Black 3.3V power pin P9_3 to MAX9744 Vi2c pin.
*   BeagleBone Black GND pin P9_1 to MAX9744 GND pin.
*   BeagleBone Black SCL pin P9_19 to MAX9744 SCL pin.
*   BeagleBone Black SDA pin P9_20 to MAX9744 SDA pin.

Make sure you don't have a device tree overlay enabled which might interfere with
the BBB's default I2C bus above.  See this guide for more information device tree
overlays:
https://learn.adafruit.com/introduction-to-the-beaglebone-black-device-tree/overview

## Installation & Example Usage

Before you get started make sure you've assembled and tested your MAX9744 board.
Follow the guide here for more information:
https://learn.adafruit.com/adafruit-20w-stereo-audio-amplifier-class-d-max9744/overview

Make sure your board is connected to the internet, then connect to its command
line terminal and run the following commands (assuming a Debian-based operating
system like Raspbian on the Pi, or Debian on the BeagleBone Black):

    sudo apt-get update
    sudo apt-get install -y python-dev build-essential python-smbus git
    cd ~
    git clone https://github.com/adafruit/Adafruit_Python_MAX9744.git
    cd Adafruit_Python_MAX9744
    sudo python setup.py install

That's it, the library should be installed and ready to use!  To run the
provided simpletest.py example that demonstrates changing the volume of the MAX9744
run the following commands (from inside the Adafruit_Python_MAX9744 directory
where the software was downloaded):

    cd examples
    sudo python simpletest.py

The example will set the volume to a moderate level (32 out of 63), mute it,
and ramp it up and down.
