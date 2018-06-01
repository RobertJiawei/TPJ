from time import ctime
import RPi.GPIO as GPIO

def setUp():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(11,GPIO.OUT)
	        
	
def LED1(state):
	if state: // True
		
	else: