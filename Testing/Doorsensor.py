import RPi.GPIO as GPIO
import time

def setup():
    doorsensor_pin = 12
    buzzer_pin = 40

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(doorsensor_pin,GPIO.IN,GPIO.PUD_UP)
    GPIO.setup(buzzer_pin,GPIO.OUT)

def buzzeron():
        GPIO.output(40,0)
        time.sleep(0.1)
        GPIO.output(40,1)
        time.sleep(0.1)
        GPIO.output(40,0)
        time.sleep(0.1)
        GPIO.output(40,1)
        time.sleep(0.1)
