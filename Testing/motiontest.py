from socket import *
import RPi.GPIO as GPIO


def setup():
    led_pin = 3
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

