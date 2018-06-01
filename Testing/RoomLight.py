from time import ctime
import RPi.GPIO as GPIO

def setUp():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(3,GPIO.OUT)
	        
	
def LED1(state):
	GPIO.output(led_pin, state)	
