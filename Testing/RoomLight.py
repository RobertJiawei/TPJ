from time import ctime
import RPi.GPIO as GPIO

def setUp():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(3,GPIO.OUT)
	        
	
def LED1(state):
	if state: // True
		GPIO.output(led_pin, 1)	
	else:
		GPIO.output(led_pin, 0)	
