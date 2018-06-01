import RoomLight
from socket import *
from time import ctime
import RPi.GPIO as GPIO

Servomotor.setup()

ctrCmd = ['1false','1true','2false','2true','3false','3true','wfalse','wtrue']

HOST = ''
PORT = 21567
BUFSIZE = 1024
ADDR = (HOST,PORT)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)

while True:
        print('Waiting for connection')
        tcpCliSock,addr = tcpSerSock.accept()
        print('...connected from :', addr)
        try:
                while True:
                        data = ''
                        data = tcpCliSock.recv(BUFSIZE)
                        if not data:
                                break
                        if data == ctrCmd[0]:
                                RoomLight.LED1(0)
                                print('LED1 Off')
                        if data == ctrCmd[1]:
                                RoomLight.LED1(1)
                                print('LED1 On')
        except KeyboardInterrupt:
                GPIO.cleanup()
tcpSerSock.close();
