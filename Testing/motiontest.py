import RPi.GPIO as GPIO


def setup():
    led_pin = 3
    senserOut_pin = 13

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(led_pin, GPIO.OUT)
    GPIO.setup(senserOut_pin, GPIO.IN)
