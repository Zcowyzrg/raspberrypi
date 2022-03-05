Raspbian Administration
=======================

See also:

* https://debian-handbook.info/browse/stable/sect.apt-get.html
* https://www.raspberrypi.com/documentation/computers/os.html

Commands:

    sudo apt update (takes about 1 min 30 sec on Pi 1)
    sudo apt install <pkg_name>
    apt list
    apt list | grep <pkg_name>
    apt list --installed
    apt list --upgradeable
    apt search <text>
    apt-cache search <text>
    apt show <pkg_name>
    dpkg -L <pkg_name>  -- lists files in package
    dpkg -S /usr/bin/gpioset -- find package owning the file


Extra packages:

* python3-rpi.gpio
* mtr-tiny
* gpiod
* htop
