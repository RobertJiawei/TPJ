#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

__author__ = "gus-pimylifeup"
__version__ = "1.0"
__maintainer__ = "pimylifeup.com"

pir_sensor = 11

GPIO.setmode(GPIO.BOARD)

GPIO.setup(pir_sensor, GPIO.IN)

current_state = 0
times = 0
try:
    while True:
        time.sleep(2)
        current_state = GPIO.input(pir_sensor)
        if current_state == 1:
            times+=1
            print("motion No.%s" % (times))
except KeyboardInterrupt:
    pass
finally:
    GPIO.cleanup()
