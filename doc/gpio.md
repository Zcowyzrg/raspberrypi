GPIO
====

Useful links:

* https://www.raspberrypi.org/documentation/usage/gpio/ -- or at [source](https://github.com/raspberrypi/documentation/tree/master/usage/gpio) for better picture
* https://elinux.org/RPi_Low-level_peripherals
* https://elinux.org/RPi_GPIO_Code_Samples
* https://pinout.xyz/
* https://sourceforge.net/p/raspberry-gpio-python/wiki/Home/
* https://www.beyondlogic.org/an-introduction-to-chardev-gpio-and-libgpiod-on-the-raspberry-pi/


Package gpiod
-------------

See https://manpages.debian.org/experimental/gpiod/index.html

- *gpiodetect* -- detect chip, e.g. `gpiochip0`
- *gpiofind* -- find named line (not on my old Pi)
- *gpioget* -- read line:

      gpioget gpiochip0 17 27 22

- *gpioinfo* -- lists all gpio lines, e.g. `16: led0 output`
- *gpiomon* -- monitor line for events
- *gpioset* -- set line:

      gpioset --mode=time --sec=3 gpiochip0 17=1
      gpioset --mode=wait gpiochip0 17=1 27=1 22=1
              [press Enter]


Other packages
--------------

- *rpi.gpio-common* -- "common files e.g. udev rules"
- *raspi-gpio* -- "dump the state"
- *gpio-utils* -- lsgpio, gpio-hammer, gpio-event-mon ("not useful for setting")
- *pigpio* -- metapackage
- *wiringpi* -- a well known one

