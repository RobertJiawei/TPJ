from time import ctime
import RPi.GPIO as GPIO

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(3,GPIO.OUT)
	GPIO.setup(5,GPIO.OUT)
	GPIO.setup(7,GPIO.OUT)
	        	
def LED1(state):
	GPIO.output(3, state)

def LED2(state):
	GPIO.output(5, state)

def LED3(state):
	GPIO.output(7, state)	
