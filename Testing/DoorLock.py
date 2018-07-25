import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.OUT) # for door lock control

def opendoor():
    GPIO.output(8, 1) # unlock the door
    time.sleep(10)
    GPIO.output(8,0) # lock the door
