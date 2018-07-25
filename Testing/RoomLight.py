import RPi.GPIO as GPIO  # import Raspberry Pi GPIO library as GPIO


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(3, GPIO.OUT)  # Setup on board pin#3 as room light 1 control
    GPIO.setup(5, GPIO.OUT)  # Setup on board pin#5 for room light 2 control
    GPIO.setup(7, GPIO.OUT)  # Setup on board pin#7 for room light 3 control


def LED1(state):             # turn room light 1 on if state is 1; or off if state is 0
    GPIO.output(3, state)


def LED2(state):             # turn room light 2 on if state is 1; or off if state is 0
    GPIO.output(5, state)


def LED3(state):            # turn room light 3 on if state is 1; or off if state is 0
    GPIO.output(7, state)
