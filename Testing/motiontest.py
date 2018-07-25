from socket import *       # import every function in socket library
import RPi.GPIO as GPIO    # import Raspberry Pi GPIO library as GPIO

led_pin = 37               # Setup on board pin#37 as LED output pin
senserOut_pin = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(led_pin, GPIO.OUT)
GPIO.setup(senserOut_pin, GPIO.IN)

HOST = '192.168.43.5'
PORT = 1237
ADDR = (HOST, PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
    conn, addr = tcpSerSock.accept()
    if GPIO.input(senserOut_pin):
        print("Yes")
        conn.send("Yes".encode())
    else:
        print("No")
        conn.send("No".encode())

