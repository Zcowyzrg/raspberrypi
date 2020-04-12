RPi Configuration
==================

See also: https://www.raspberrypi.org/documentation/configuration/

Boot options
------------

Edit `config.txt` on FAT partition or at `/boot/config.txt`

    disable_overscan=1
    hdmi_pixel_encoding=2

The raspi-config tool
---------------------

### Enable SSH server

Run `sudo raspi-config`. Choose `5 Interfacing options` &rarr; `P2 SSH - enable`

Another option: create empty `ssh` file on `boot` partition (not checked).

Another option: just use `systemctl`.

See also:
* https://www.raspberrypi.org/documentation/remote-access/ssh/
* https://www.raspberrypi.org/documentation/configuration/wireless/headless.md

Other configuration
-------------------

- zeroconf - avahi daemon is running by default. Enables host discovery by name with Windows.
- ssh - not enabled by default.

Show MAC address:

    $ ip link

    2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> (...)
        link/ether b8:27:eb:ea:86:de brd ff:ff:ff:ff:ff:ff
