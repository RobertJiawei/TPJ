import RPi.GPIO as GPIO
import time

def setup():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11,GPIO.IN,GPIO.PUD_UP) # for door sensor input
    GPIO.setup(40,GPIO.OUT) # for buzzer control

def buzzeron():
        GPIO.output(40,0) # turn off the buzzer 
        time.sleep(0.1)
        GPIO.output(40,1) # turn on the buzzer 
        time.sleep(0.1)
        GPIO.output(40,0)
        time.sleep(0.1)
        GPIO.output(40,1)
        time.sleep(0.1)
