from time import ctime
import RPi.GPIO as GPIO

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(3,GPIO.OUT)
	        
	
def LED1(state):
	GPIO.output(3, state)	
