import RoomLight
import servotest as window
from socket import *
import time
import RPi.GPIO as GPIO

RoomLight.setup()


ctrCmd = ['room1on','room1off','room2on','room2off','room3on','room3off', 'windowopen','windowclose']

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
                elif cmd[10:-1] == ctrCmd[6]:
                        window.leftturn()
                        print("WINDOW OPENING")
                elif cmd[10:-1] == ctrCmd[7]:
                        window.rightturn()
                        print("WINDOW CLOSING")
        except KeyboardInterrupt:
                GPIO.cleanup()
                
tcpSerSock.close();