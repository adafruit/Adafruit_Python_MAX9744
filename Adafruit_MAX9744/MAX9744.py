# Copyright (c) 2015 Adafruit Industries
# Author: Tony DiCola
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.


# Default I2C address for device.
MAX9744_I2CADDR         = 0x4B


class MAX9744(object):
    """Class to represent an Adafruit MAX9744 20 watt stereo amplifier with
    digital volume control.
    """

    def __init__(self, address=MAX9744_I2CADDR, i2c=None, **kwargs):
        """Initialize MAX9744 device on the specified I2C address and bus number.
        Address defaults to 0x4B and bus number defaults to the appropriate bus
        for the hardware.
        """
        # Initialize I2C bus and get a reference to the MAX9744 device.
        if i2c is None:
            import Adafruit_GPIO.I2C as I2C
            i2c = I2C
        self._device = i2c.get_i2c_device(address, **kwargs)

    def set_volume(self, value):
        """Set volume to the provided value which should be a number from 0 (muted)
        to 63 (maximum volume).
        """
        assert value >= 0 and value <= 63, 'Volume value must be between 0 and 63 inclusive.'
        # Send the volume set command with the provided value.
        self._device.writeRaw8(value & 0b111111)

    def increase_volume(self):
        """Increase the volume by one step."""
        # Send volume increase command: 0b11000100
        self._device.writeRaw8(0b11000100)

    def decrease_volume(self):
        """Decrease the volume by one step."""
        # Send volume decrease command: 0b11000101
        self._device.writeRaw8(0b11000101)
