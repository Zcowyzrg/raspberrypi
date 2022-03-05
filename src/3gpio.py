#!/usr/bin/env python

import RPi.GPIO as g

PINS = [17, 27, 22]
help_message = 'Specify GPIO values as 000, 001, etc. Type q for quit or anything for this help message'
running = True

g.setmode(g.BCM)
g.setup(PINS, g.OUT, initial=g.LOW)

for a, b in g.RPI_INFO.iteritems():
    print('-- %s : %s' % (a, b))

print(help_message)

while running:
    gpio_state = ''.join([str(g.input(pin)) for pin in PINS])
    ans = raw_input(gpio_state + '> ')
    if len(ans) == len(PINS) and all(ans[i] == '0' or ans[i] == '1' for i in range(len(PINS))):
        g.output(PINS, [g.HIGH if pin == '1' else g.LOW for pin in ans])
    elif len(ans) == 1 and ans[0] == 'q':
        running = False
    else:
        print(help_message)

g.cleanup(PINS)
