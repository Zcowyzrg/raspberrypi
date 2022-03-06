#!/usr/bin/env python

import atexit
import time
from bottle import abort, get, post, request, route, run, static_file
import RPi.GPIO as g

IN1 = 17  # RPi gpio for relay #1
IN2 = 27
ACTIVE = g.LOW
INACTIVE = g.HIGH

def gpio_status():
    status = str(g.input(IN1)) + str(g.input(IN2))
    print(status)
    return status + "\n"

@route('/gpio')
def gpio_static():
    return static_file('index.html', root='.')

@route('/gpio/get')
def gpio_get():
    return gpio_status()

@post('/gpio/set')
def gpio_set():
    action = request.forms.get('action')
    print(f'action={action}')
    if action == 'debug':
        g.output(IN1, INACTIVE)
    elif action == 'bypass':
        g.output(IN1, ACTIVE)
    elif action == 'reset':
        g.output(IN2, ACTIVE)
        time.sleep(0.5)
        g.output(IN2, INACTIVE)
    else:
        abort(400, "Invalid argument")
    return gpio_status()

g.setmode(g.BCM)
g.setup([IN1, IN2], g.OUT, initial=g.HIGH)  # relay is active-low
atexit.register(g.cleanup, [IN1, IN2])
run(host='0.0.0.0', port=8080)

