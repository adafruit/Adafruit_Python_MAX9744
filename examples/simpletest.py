# Simple example of using the MAX9744 volume control over I2C.
# Author: Tony DiCola
import time

from Adafruit_MAX9744 import MAX9744


# Maximum volume level that will be used in this example.  Can be a value from
# 0 (muted) to 63 (max volume--warning, it can be LOUD!).
MAX_VOLUME = 32


# Create a MAX9744 class instance.  With no arguments to the initializer it will
# pick a default I2C bus and device address to look for the MAX9744.
# On a Raspberry Pi connect the MAX9744 SCL and SDA pins to the Pi GPIO header
# SCL and SDA pins.  Make sure I2C has been enabled too, see:
#  https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c
# On a BeagleBone Black the default I2C bus is /dev/i2c-1 which is exposed on
# SCL pin P9_19 and SDA pin P9_20.
amp = MAX9744()

# Alternatively you can specify the I2C bus and/or device address by providing
# optional parameter values:
#amp = MAX9744(busnum=2, address=0x4C)

# Explicitly set the volume using the set_volume function.  This takes a value
# from 0 to 63 (inclusive) where 0 is muted and 63 is maximum volume (warning,
# it can get LOUD!).
print('Setting volume to {0} for 5 seconds...'.format(MAX_VOLUME))
amp.set_volume(MAX_VOLUME)
time.sleep(5)

print('Setting volume to 0 (muted) for 5 seconds...')
amp.set_volume(0)
time.sleep(5)

print('Ramping volume up and down from 0 to {0}...'.format(MAX_VOLUME))
print('Press Ctrl-C to quit.')
while True:
    # Ramp up and hold each level for a second.
    for i in range(MAX_VOLUME):
        # Use the increase_volume function to bump up a level.
        print('Volume level increased.')
        amp.increase_volume()
        time.sleep(1)
    # Ramp down and hold each level for a second.
    for i in range(MAX_VOLUME):
        # Use the decrease_volume function to bump down a level.
        print('Volume level decreased.')
        amp.decrease_volume()
        time.sleep(1)
