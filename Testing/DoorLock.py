import RPi.GPIO as GPIO  # import Raspberry Pi GPIO library as GPIO
import time  # import time library

def setup(): # set up GPIO 8
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.OUT)  # for door lock control; set GPIO 8 as an output
    
def opendoor(): # unlock the door then lock the door in 10s
    GPIO.output(8, 1)  # Set pin high to open the door
    time.sleep(10)
    GPIO.output(8, 0)  # After 10 seconds, the door will automatic close
