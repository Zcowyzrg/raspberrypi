Windows connection sharing
==========================

We will be _sharing_ the WiFi connection and _connecting_ Raspberry Pi through Ethernet cable. Open Control Panel &rarr; Network And Sharing Centre &rarr; Change Adapter Settings (or Network Connections).

![Network Connections](win-network-adapters.png)

Select WiFi, right-click for Properties and select "Allow other network users to connect through this computer's internet connection". Choose "Ethernet" as Home networking connection. Windows will allocate a static 192.168.137.1 IP adress to the "Ethernet" adapter.

![WiFi Properties](win-wifi-properties.png)

Connect Raspberry Pi with Ethernet cable and boot it. The DHCP client is already enabled and will configure the IP address. The address will be printed on the RPi console, e.g. 192.168.137.248.

Finding Raspberry Pi address
----------------------------

If you run the Raspberry Pi headless, this is what you can do to find it's IP address:

Use `ipconfig` to find your "Ethernet" adapter IP address:

    Ethernet adapter Ethernet:
    IPv4 Address. . . . . . . . . . . : 192.168.137.1

Use `arp -a` to list cached IP addresses. If you know your Pi's MAC address (`b8-27-eb-ea-86-de` in this case), you know it's IP address.

    Interface: 192.168.137.1 --- 0x12
      Internet Address      Physical Address      Type
      192.168.137.248       b8-27-eb-ea-86-de     static

These commands work because Pi runs `avahi` zeroconf daemon for host name discovery:

    ping raspberrypi             # uses IPv6
    ping -4 raspberrypi
    ping -4 raspberrypi.local
    ssh pi@raspberrypi
    ssh pi@raspberrypi.local

From PI, you should be able to `ping 8.8.8.8` (Google DNS server) or use `mtr 8.8.8.8`
