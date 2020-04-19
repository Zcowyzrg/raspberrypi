#!/usr/bin/env python2

import time
import RPi.GPIO as g

WR_CHAN = 17
RD_CHAN = 27
DELAY = 2

g.setmode(g.BCM)
g.setup(WR_CHAN, g.OUT)
g.setup(RD_CHAN, g.IN, pull_up_down=g.PUD_UP)

for a, b in g.RPI_INFO.iteritems():
    print '-- %s : %s' % (a, b)
print 'Toggling GPIO %d every %d second:' % (WR_CHAN, DELAY)

for val in (g.LOW, g.HIGH) * 5:
    g.output(WR_CHAN, val)
    print 'Out(%d)=%d In(%d)=%d' % (WR_CHAN, val, RD_CHAN, g.input(RD_CHAN))
    time.sleep(DELAY)

g.cleanup(WR_CHAN)
g.cleanup(RD_CHAN)
