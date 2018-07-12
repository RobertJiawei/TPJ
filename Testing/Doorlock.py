import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.OUT)

def opendoor():
    GPIO.output(8, 1)
    time.sleep(10)
    GPIO.output(8,0)