import os
import RoomLight
import servotest as window
from socket import *
import time
import RPi.GPIO as GPIO

RoomLight.setup()
window.setup()

ctrCmd = ['1true','1false','2true','2false','3true','3false', 'windowtrue','windowfalse', 'v', 'vt']

HOST = '192.168.43.5'
PORT = 1234
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
                cmd = str(data)
                print(cmd[10:-1])
                if cmd[10:-1] == ctrCmd[0]:
                        RoomLight.LED1(1)
                        print("ROOM 1 ON!")
                elif cmd[10:-1] == ctrCmd[1]:
                        RoomLight.LED1(0)
                        print("ROOM 1 OFF")
                elif cmd[10:-1] == ctrCmd[2]:
                        RoomLight.LED2(1)
                        print("ROOM 2 ON!")
                elif cmd[10:-1] == ctrCmd[3]:
                        RoomLight.LED2(0)
                        print("ROOM 2 OFF")
                elif cmd[10:-1] == ctrCmd[4]:
                        RoomLight.LED3(1)
                        print("ROOM 3 ON!")
                elif cmd[10:-1] == ctrCmd[5]:
                        RoomLight.LED3(0)
                        print("ROOM 3 OFF")
                elif cmd[8:-1] == ctrCmd[6]:
                        window.leftturn()
                        print("WINDOW OPENING")
                elif cmd[10:-1] == ctrCmd[7]:
                        window.rightturn()
                        print("WINDOW CLOSING")
                elif cmd[10:-1] == ctrCmd[8]:
                        os.system("raspivid -o - -t 0 -hf -w 800 -h 400 -fps 24 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:1235}' :demux=h264")
                elif cmd[10:-1] == ctrCmd[9]:
                        print("stop")
                        tcpSerSock.close()
        except KeyboardInterrupt:
                GPIO.cleanup()
                
#tcpSerSock.close()