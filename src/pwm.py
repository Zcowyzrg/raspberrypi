#!/usr/bin/env python2

import time
import RPi.GPIO as g

CHANNEL = 17
DELAY = 2

g.setmode(g.BCM)
g.setup(CHANNEL, g.OUT)
pwm = g.PWM(CHANNEL, 500)

pwm.start(10)
print '10%%'
time.sleep(3)
pwm.ChangeDutyCycle(50)
print '50%%'
time.sleep(3)
pwm.ChangeDutyCycle(90)
print '90%%'
time.sleep(3)
pwm.stop()

g.cleanup(CHANNEL)
