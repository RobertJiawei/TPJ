import RPi.GPIO as GPIO

def setup():
	GPIO.setmode(GPIO.BOARD)
	GPIO.setup(3,GPIO.OUT) # for room light 1 control
	GPIO.setup(5,GPIO.OUT) # for room light 2 control
	GPIO.setup(7,GPIO.OUT) # for room light 3 control
	        	
def LED1(state): # turn room light 1 on if state is 1; or off if state is 0
	GPIO.output(3, state)

def LED2(state):
	GPIO.output(5, state)

def LED3(state):
	GPIO.output(7, state)	
