#!/usr/bin/env python
'''
Setup the Circuit:
1. Adjust appropriate Sensitivity and Duration of the sensor
2. Connect the pins: GND-Out-Vcc
3. Research for correct Vcc: 5 or 3.3V
4. Add a current-limiting R to the Out-sensorOut_pin
'''

import RPi.GPIO as GPIO
import time

senserOut_pin = 11                       # GPIO 2
GPIO.setmode(GPIO.BOARD)
GPIO.setup(senserOut_pin, GPIO.IN)      # GPIO 2 to be an input

times = 0
try:
    while True:
        time.sleep(2)
        if GPIO.input(senserOut_pin):
            times+=1
            print("motion No.%s" % (times))
except KeyboardInterrupt:
    pass
except:
    GPIO.cleanup()
