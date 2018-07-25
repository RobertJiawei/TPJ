import RPi.GPIO as GPIO                     # import Raspberry Pi GPIO library as GPIO
import time                                 # import time library

def setup():                                # set up on-board pins 11 and 40
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(11, GPIO.IN, GPIO.PUD_UP)    # set on board pin 11 as the door sensor input
    GPIO.setup(40, GPIO.OUT)                # set on board pin 40 for buzzer control

def buzzeron():                             # make the buzzer to produce a 2-beep sound
    GPIO.output(40, 0)                      # turn on the buzzer
    time.sleep(0.1)
    GPIO.output(40, 1)                      # turn off the buzzer
    time.sleep(0.1)
    GPIO.output(40, 0)                    
    time.sleep(0.1)
    GPIO.output(40, 1)                    
    time.sleep(0.1)
