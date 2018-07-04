import RPi.GPIO as GPIO

doorsensor_pin = 12

GPIO.setmode(GPIO.BOARD)
GPIO.setup(doorsensor_pin,GPIO.IN)

while True:
    if GPIO.input(doorsensor_pin):
        print("Door is closed")
    else:
        print("Door is opened")