import RPi.GPIO as GPIO
import time

def setup():
    doorsensor_pin = 12
    buzzer_pin = 40

    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(doorsensor_pin,GPIO.IN,GPIO.PUD_UP)
    GPIO.setup(buzzer_pin,GPIO.OUT)

    while True:
        if GPIO.input(doorsensor_pin):
            print("Door is opened")
            GPIO.output(buzzer_pin,0)
            time.sleep(0.1)
            GPIO.output(buzzer_pin,1)
            time.sleep(0.1)
            GPIO.output(buzzer_pin,0)
            time.sleep(0.1)
            GPIO.output(buzzer_pin,1)
            time.sleep(0.1)
            while GPIO.input(doorsensor_pin):
                print("door opened")
        else:
            GPIO.output(buzzer_pin,1)
            print("Door is closed")
