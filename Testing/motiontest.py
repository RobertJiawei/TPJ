#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

senserOut_pin = 11                       # GPIO 2
GPIO.setmode(GPIO.BOARD)
GPIO.setup(senserOut_pin, GPIO.IN)      # GPIO 2 to be an input

times = 0
try:
    while True:
        time.sleep(2)
        print(GPIO.input(senserOut_pin))
        """if GPIO.input(senserOut_pin):
            times+=1
            print("motion No.%s" % (times))"""
except KeyboardInterrupt:
    pass
except:
    GPIO.cleanup()

"""while True:
    print(GPIO.input(senserOut_pin))"""
