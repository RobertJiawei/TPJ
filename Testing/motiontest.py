#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

led_pin = 3                 
senserOut_pin = 11                       

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(senserOut_pin, GPIO.IN)     

try:
    while True:
        if GPIO.input(senserOut_pin):
            GPIO.output(led_pin, 1)
            time.sleep(1)
        else:
            GPIO.output(led_pin, 0)

except KeyboardInterrupt:
    pass
except:
    GPIO.cleanup()
