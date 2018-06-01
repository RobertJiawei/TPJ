import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(2.5)

def leftturn():
	p.ChangeDutyCycle(2.5)  # turn towards 90 degree
	print("left")
	time.sleep(1) # sleep 1 second

def rightturn():
	p.ChangeDutyCycle(12.5)  # turn towards 90 degree
	print("right")
	time.sleep(1) # sleep 1 second

try:
        while True:
		turn = raw_input("left or right")
		if(turn == "left"):
			leftturn()
		else:
			rightturn()
except KeyboardInterrupt:
	p.stop()
        GPIO.cleanup()
