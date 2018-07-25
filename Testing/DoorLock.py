import RPi.GPIO as GPIO  # import Raspberry Pi GPIO library as GPIO
import time  # import time library


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.OUT)  # Setup on board pin#8 as door lock control


def opendoor():
    GPIO.output(8, 1)  # Set pin high to open the door
    time.sleep(10)
    GPIO.output(8, 0)  # After 10 seconds, the door will automatic close
