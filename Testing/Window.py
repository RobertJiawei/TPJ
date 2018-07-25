import RPi.GPIO as GPIO    # import Raspberry Pi GPIO library as GPIO


def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)  # Set up on board 12 as servo motor input
    global p
    p = GPIO.PWM(12, 50)      # Set up Global p as PWM output and set frequency as 50Hz
    p.start(12.5)             # Start PWM output and set initial length at 12.5 milliseconds


def leftturn():
    p.ChangeDutyCycle(7.5)  # turn towards 90 degree
    print("left")


def rightturn():
    p.ChangeDutyCycle(12.5)  # turn towards 90 degree
    print("right")
