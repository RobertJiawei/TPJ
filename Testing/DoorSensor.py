import RPi.GPIO as GPIO  # import Raspberry Pi GPIO library as GPIO
import time  # import time library


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.IN, GPIO.PUD_UP)  # Set up on board pin#11 as door sensor input
    GPIO.setup(40, GPIO.OUT)  # Set up on board pin#40 for buzzer control


def buzzeron():
    GPIO.output(40, 0)  # turn on the buzzer
    time.sleep(0.1)
    GPIO.output(40, 1)  # turn off the buzzer
    time.sleep(0.1)
    GPIO.output(40, 0)  # turn on the buzzer
    time.sleep(0.1)
    GPIO.output(40, 1)  # turn off the buzzer
    time.sleep(0.1)
