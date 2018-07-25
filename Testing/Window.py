import RPi.GPIO as GPIO    # import Raspberry Pi GPIO library as GPIO

def setup():                  # set up GPIO 12
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12, GPIO.OUT)  # set up on board 12 as servo motor input
    global p
    p = GPIO.PWM(12, 50)      # set up Global p as PWM output and set frequency as 50Hz
    p.start(12.5)             # start PWM output and set initial length at 12.5 milliseconds

def leftturn(): # turn to 90 degree
    p.ChangeDutyCycle(7.5) 
    print("left")

def rightturn(): # turn to 180 degree
    p.ChangeDutyCycle(12.5) 
    print("right")
