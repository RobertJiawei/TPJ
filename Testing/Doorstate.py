from socket import *       # import every function in socket library
import RPi.GPIO as GPIO    # import Raspberry Pi GPIO library as GPIO
import Doorsensor          # import Doorsensor.py as a library
import time                # import time library


Doorsensor.setup()         # Run Doorsensor setup function

HOST = '192.168.43.5'
PORT = 1236
ADDR = (HOST, PORT)        # Setup socket server information (IP address, port number and size of the package)

tcpSerSock = socket(AF_INET, SOCK_STREAM)    # Build a Socket based on TCP connection
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)                         # Server start to listen up to 4 client request

while True:
    print("waiting for connection")
    conn, addr = tcpSerSock.accept()         # Accept the request from client and build connection
    print("..... connected .....")

    if GPIO.input(11):                       # Check GPIO#11 logic level. if it is high, the door is opened
        print("Door opened")
        Doorsensor.buzzeron()                # Buzzer will make two 'bip' sound when door is opened
        conn.send("open".encode('utf-8'))    # Send message "open" back to client
        print("Door opened")
        while GPIO.input(11):                # When door is open, the buzzer only sound one time
            pass                             # The door status will stay open unless the logic level become low
    else:                                    # If it is low, the door is closed
        conn.send("close".encode('utf-8'))   # Send message "close" back to client
        print("Door closed")
    time.sleep(1)                            # The time between each check is 1 second
