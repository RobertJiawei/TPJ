#!/usr/bin/env python

import RPi.GPIO as GPIO
import time

motionFeedback_pinOut = 3                       # GPIO 2
GPIO.setmode(GPIO.BCM)
GPIO.setup(motionFeedback_pinOut, GPIO.IN)      # GPIO 2 to be an input

times = 0
try:
    while True:
        time.sleep(2)
        if GPIO.input(motionFeedback_pinOut):
            times+=1
            print("motion No.%s" % (times))
except KeyboardInterrupt:
    pass
except:
    GPIO.cleanup()
