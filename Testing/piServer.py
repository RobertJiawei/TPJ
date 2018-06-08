import RoomLight
from socket import *
import time
import RPi.GPIO as GPIO

RoomLight.setup()

#ctrCmd = ['1false','1true','2false','2true','3false','3true','wfalse','wtrue']
#ctrCmd = ['1']
HOST = '192.168.43.5'
PORT = 21565
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(10)

while True:
        print('Waiting for connection')
        tcpCliSock,addr = tcpSerSock.accept()
        print('...connected from :', addr)
        try:
                #while True:
                data = tcpCliSock.recv(BUFSIZE)
                print(data[2:])
                if data[2:] == "b'room1on'":
                        RoomLight.LED1(1)
                        print("ROOM 1 ON!")
                elif data[2:] == "b'room1off'":
                        RoomLight.LED1(0)
                        print("ROOM 1 OFF")
                """elif data[2:] == "room2on":
                        RoomLight.LED2(1)
                        print("ROOM 2 ON!")
                elif data[2:] == "room2off":
                        RoomLight.LED2(0)
                        print("ROOM 2 OFF")
                elif data[2:] == "room3on":
                        RoomLight.LED3(1)
                        print("ROOM 3 ON!")
                elif data[2:] == "room3off":
                        RoomLight.LED3(0)
                        print("ROOM 3 OFF")"""
        except KeyboardInterrupt:
                GPIO.cleanup()
                
tcpSerSock.close();