import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(22, GPIO.OUT)

p = GPIO.PWM(22, 50)

p.start(0)

try:
        while True:
		p.ChangeDutyCycle(7.5)  # turn towards 90 degree
		time.sleep(1) # sleep 1 second
		"""p.ChangeDutyCycle(12.5) # turn towards 180 degree
        time.sleep(1) # sleep 1 second 
        """
except KeyboardInterrupt:
	p.stop()
        GPIO.cleanup()