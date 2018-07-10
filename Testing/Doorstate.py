from socket import *
import RPi.GPIO as GPIO
import Doorsensor
import time

HOST = '192.168.43.5'
PORT = 1236
BUFSIZE = 1024
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    print("waiting for connection")
    conn, addr = tcpSerSock.accept()
    print("..... connected .....")
    if GPIO.input(11):
        print("Door opened")
        Doorsensor.buzzeron()
        conn.send("open".encode())
        print("door open")
        while GPIO.input(11):
            pass
    else:
        conn.send("close".encode())
        pass
        print("Door is closed")
    print("door!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    time.sleep(1)
