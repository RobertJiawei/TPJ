import RPi.GPIO as GPIO  # import Raspberry Pi GPIO library as GPIO
import time  # import time library

def setup(): # set up on-board pin 8
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(8, GPIO.OUT)  # for door lock control; set on-board pin 8 as an output
    
def opendoor(): # unlock the door then lock the door in 10s
    GPIO.output(8, 1)  # set on-board pin 8 high to unlock the door
    time.sleep(10)
    GPIO.output(8, 0)  # set on-board pin 8 low to lock the door
