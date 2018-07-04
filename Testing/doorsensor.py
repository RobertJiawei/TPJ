import RPi.GPIO as GPIO
import time

doorsensor_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(doorsensor_pin,GPIO.IN,GPIO.PUD_UP)

while True:
    if GPIO.input(doorsensor_pin):
        print("Door is opened")
    else:
        print("Door is closed")
    time.sleep(0.5)