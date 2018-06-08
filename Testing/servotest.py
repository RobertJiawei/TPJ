import RPi.GPIO as GPIO
import time

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(12, GPIO.OUT)
	#p = GPIO.PWM(12, 50)
	#p.start(2.5)

def leftturn():
	p = GPIO.PWM(12, 50)
	p.start(2.5)
	p.ChangeDutyCycle(2.5)  # turn towards 90 degree
	print("left")
	time.sleep(1) # sleep 1 second

def rightturn():
	p = GPIO.PWM(12, 50)
	p.start(2.5)
	p.ChangeDutyCycle(12.5)  # turn towards 90 degree
	print("right")
	time.sleep(1) # sleep 1 second

