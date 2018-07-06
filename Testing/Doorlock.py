import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(15, GPIO.OUT)

def opendoor():
    GPIO.output(15, 0)
    time.sleep(10)
    GPIO.output(15,1)