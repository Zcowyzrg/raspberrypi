Raspbian Administration
=======================

See also:

* https://debian-handbook.info/browse/stable/sect.apt-get.html
* https://www.raspberrypi.org/documentation/raspbian/updating.md

Commands:

    sudo apt update (takes about 1 min 30 sec)
    sudo apt install python3-rpi.gpio
    apt list
    apt list | grep <pkgname>
    apt list --installed
    apt list --upgradeable
    apt search <text>
    apt show <pkgname>
	dpkg -L <pkgname>  -- lists files in package
    dpkg -S /usr/bin/gpioset -- find package owning the file


Extra packages:

* python3-rpi.gpio
* mtr-tiny
* gpiod
