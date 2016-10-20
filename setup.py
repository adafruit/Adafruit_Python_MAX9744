try:
    # Try using ez_setup to install setuptools if not already installed.
    from ez_setup import use_setuptools
    use_setuptools()
except ImportError:
    # Ignore import error and assume Python 3 which already has setuptools.
    pass

from setuptools import setup, find_packages

setup(name              = 'Adafruit_MAX9744',
      version           = '1.0.2',
      author            = 'Tony DiCola',
      author_email      = 'tdicola@adafruit.com',
      description       = 'Library for controlling the MAX9744 class D amplifier with I2C volume control on a Raspberry Pi or Beaglebone Black.',
      license           = 'MIT',
      url               = 'https://github.com/adafruit/Adafruit_Python_MAX9744/',
      dependency_links  = ['https://github.com/adafruit/Adafruit_Python_GPIO/tarball/master#egg=Adafruit-GPIO-0.9.0'],
      install_requires  = ['Adafruit-GPIO>=0.9.0'],
      packages          = find_packages())
