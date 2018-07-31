from socket import *       # import every function in socket library
import RPi.GPIO as GPIO    # import Raspberry Pi GPIO library as GPIO
import RoomLight           # import RoomLight.py as a library

led_pin = 37               
senserOut_pin = 13        

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)            # set on-board pin 37 as an LED output pin
GPIO.setup(senserOut_pin, GPIO.IN)       # set on-board pin 13 as the sensor input pin

RoomLight.setup()

HOST = '192.168.43.5'
PORT = 1237
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    conn, addr = tcpSerSock.accept()      # receive data from MyHome application 
    if GPIO.input(senserOut_pin):         # sensor is triggered
        GPIO.output(led_pin, 1)           # turn on the LED on the door
        # print("Yes")
        conn.send("1".encode())           # send "1" back to MyHome application
        RoomLight.LED4(1)                 # If someone is near the door, the motion light will be on
    else:                                 # sensor is not triggered
        GPIO.output(led_pin, 0)           # turn off the LED
        # print("No")
        conn.send("0".encode())           # send "0" back to MyHome
        RoomLight.LED4(0)                 # If nobody is near the door, the motion light will be off
