from socket import *       # import every function in socket library
import RPi.GPIO as GPIO    # import Raspberry Pi GPIO library as GPIO
import DoorSensor          # import Doorsensor.py as a library
import time                # import time library

DoorSensor.setup()         # run Doorsensor setup function

HOST = '192.168.43.5'
PORT = 1236
ADDR = (HOST, PORT)        # set up socket server information (IP address, port number and size of the package)

tcpSerSock = socket(AF_INET, SOCK_STREAM)    # build a Socket based on TCP connection
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)                         # server start to listen up to 4 client request

while True:
    print("waiting for connection")
    conn, addr = tcpSerSock.accept()         # accept the request from client and build connection
    print("..... connected .....")

    if GPIO.input(11):                       # check GPIO#11 logic level. if it is high, the door is opened
        print("Door opened")
        DoorSensor.buzzeron()                # buzzer will make two 'bip' sound when door is opened
        conn.send("1".encode('utf-8'))       # send message "1" back to client
        print("Door opened")
        while GPIO.input(11):                # when door is open, the buzzer only sound one time
            pass                             # the door status will stay open unless the logic level become low
    else:                                    # if it is low, the door is closed
        conn.send("0".encode('utf-8'))   # send message "0" back to client
        print("Door closed")
    time.sleep(1)                            # the time between each check is 1 second
