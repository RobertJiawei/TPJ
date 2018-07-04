import RPi.GPIO as GPIO
import time

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(12, GPIO.OUT) # set up GPIO 12 as servo motor input
	global p
	p = GPIO.PWM(12, 50)
	p.start(2.5)

def leftturn():
	p.ChangeDutyCycle(2.5)  # turn towards 90 degree
	print("left")

def rightturn():
	p.ChangeDutyCycle(12.5)  # turn towards 90 degree
	print("right")
