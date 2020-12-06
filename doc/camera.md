
# Streaming camera over network - raw h264

* https://picamera.readthedocs.io/en/release-1.13/fov.html (camera hardware)
* https://www.raspberrypi.org/forums/viewtopic.php?t=235684
* https://www.raspberrypi.org/documentation/raspbian/applications/camera.md
* https://wiki.videolan.org/Media_resource_locator/
* https://wiki.marcluerssen.de/index.php?title=Raspberry_Pi/Camera_streaming

```
    raspivid -a 12 -stm -ih -n -t 0 -awb greyworld -md 4 -vf -l -o tcp://0.0.0.0:8080
```

# Windows - VLC

Open Stream: `tcp/h264://192.168.0.110:8080`

Command line: `vlc.exe --demux h264 tcp://192.168.0.110:8080`

# Still photos

    raspistill -o c1.jpg -n -ex auto -awb greyworld -md 6 -t 3000 -vf
    raspistill --ISO 800 -ex night -awb tungsten -md 2 -o pic.jpg -t 3000 -n
    raspistill --ISO 800 -ex night -awb tungsten -md 2 -td -t 3000 -n
    raspistill --ISO 100 -ex night -awb tungsten -md 2 -td -t 3000 -n -o p2.jpg
    raspistill --ISO 100 -ex night -awb tungsten -md 2  -t 3000 -n -ts
    raspistill --ISO 100 -ex night -awb tungsten -md 2  -t 3000 -n -o p2.jpg
    raspistill --ISO 100 -ex night -awb grayworld -md 2  -t 3000 -n -o p3.jpg
    raspistill --ISO 100 -ex night -awb greyworld -md 2  -t 3000 -n -o p3.jpg
    raspistill --ISO 100 -ex off -awb greyworld -md 2  -t 3000 -n -o p4.jpg
    raspistill --ISO 100 -ex verylong -awb greyworld -md 2 -t 2000 -n -o p4.jpg
    raspistill --ISO 100 -ex verylong -awb greyworld -md 2 -t 2000 -n -ss 1000000 -o p5.jpg
    raspistill --ISO 100 -ex verylong -awb greyworld -md 2 -t 2000 -n -ss 500000 -o p6.jpg
    raspistill --ISO 100 -ex off -awb off -md 2 -t 2000 -n -ss 500000 -o p7.jpg
    raspistill --ISO 100 -ex verylong -awb off -md 2 -t 1000 -n -ss 500000 -o p7a.jpg
    raspistill --ISO 100 -ex off -awb greyworld -md 2 -t 2000 -n -ss 500000 -o p7.jpg
    raspistill --ISO 100 -ex off -awb off -md 2 -t 2000 -n -ss 500000 -o p8.jpg
    raspistill --ISO 100 -ex off -awb off -md 2 -t 1000 -n -ss 500000 -o p9.jpg

# Timelapse

```
raspistill --ISO 100 -ex off -awb off -md 2 -t 20000 -n -tl 7000 -ss 3000000 -o 'tl%03d.jpg'
```

# Long shots

 * https://www.raspberrypi.org/forums/viewtopic.php?t=132944
 * https://www.raspberrypi.org/forums/viewtopic.php?t=220544

```
 raspistill --ISO 800 -ex off -awb off -awbg 1,2.5 -md 2 -t 500 -ss 8000000 -n -o night.jpg
```
