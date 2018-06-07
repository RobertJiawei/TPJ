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
                print(data)
                time.sleep(1)
                        '''
                        if not data:
                                break
                        if data == ctrCmd[0]:
                                RoomLight.LED1(0)
                                print('LED1 Off')
                        if data == ctrCmd[1]:
                                RoomLight.LED1(1)
                                print('LED1 On')
                                '''
        except KeyboardInterrupt:
                GPIO.cleanup()
                
tcpSerSock.close();