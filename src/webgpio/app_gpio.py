#!/usr/bin/env python

import atexit
import time
from bottle import abort, post, request, route, run, static_file
import RPi.GPIO as g

IN1 = 17  # RPi gpio for relay #1
IN2 = 27
ACTIVE = g.LOW
INACTIVE = g.HIGH

@route('/gpio')
def gpio_static():
    return static_file('index.html', root='.')

@post('/gpio/set')
def gpio_set():
    action = request.forms.get('action')
    print(f'action={action}')
    if action == 'debug':
        g.output(IN1, INACTIVE)
        ret = g.input(IN1)
    elif action == 'bypass':
        g.output(IN1, ACTIVE)
        ret = g.input(IN1)
    elif action == 'reset':
        g.output(IN2, ACTIVE)
        time.sleep(0.5)
        g.output(IN2, INACTIVE)
        ret = g.input(IN2)
    else:
        abort(400, "Invalid argument")
    return str(ret) + "\n"

g.setmode(g.BCM)
g.setup([IN1, IN2], g.OUT, initial=g.HIGH)  # relay is active-low
atexit.register(g.cleanup, [IN1, IN2])
run(host='0.0.0.0', port=8080)

