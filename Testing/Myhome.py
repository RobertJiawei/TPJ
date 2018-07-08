import os
import RoomLight
import Window
from socket import *
import RPi.GPIO as GPIO
import Doorsensor
import threading
import time
import Doorlock
import motiontest


def doorcheck(conndoor, addrdoor):
    while True:
        if GPIO.input(11):
            print("Door opened")
            Doorsensor.buzzeron()
            conndoor.send("open".encode('utf-8'))
            while GPIO.input(11):
                pass
        else:
            print("Door is closed")
            conndoor.send("close".encode('utf-8'))
        time.sleep(1)


def motioncheck(connmotion, motionaddr):
    while True:
        if GPIO.input(13):
            print("Yes")
            connmotion.send("yes".encode('utf-8'))
        else:
            print("No")
            connmotion.send("no".encode('utf-8'))


RoomLight.setup()
Doorsensor.setup()
Window.setup()
Doorlock.setup()
motiontest.setup()


ctrCmd = ['1true', '1false', '2true', '2false', '3true',
              '3false', 'wtrue', 'wfalse', 'v', 'vt', 'd']

HOST = '192.168.43.5'
PORT = 1234
PORTreturn = 1236
BUFSIZE = 20
ADDR = (HOST, PORT)
ADDRreturn = (HOST, PORTreturn)

tcpSerSock = socket(AF_INET, SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(10)

tcpSerSockreturn = socket(AF_INET, SOCK_STREAM)
tcpSerSockreturn.bind(ADDRreturn)
tcpSerSockreturn.listen(10)

connreturn, addrreturn = tcpSerSockreturn.accept()

threads = []
tdoor = threading.Thread(target=doorcheck, args=(connreturn, addrreturn))
tmotion = threading.Thread(target=motioncheck, args=(connreturn, addrreturn))
threads.append(tdoor)
threads.append(tmotion)

for t in threads:
    t.setDaemon(True)
    t.start()

while True:
    print('Waiting for connection')
    conn, addr = tcpSerSock.accept()
    print('...connected from :', addr)

    try:
        data = conn.recv(BUFSIZE)
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
            Window.leftturn()
            print("WINDOW OPENING")
        elif cmd[10:-1] == ctrCmd[7]:
            Window.rightturn()
            print("WINDOW CLOSING")
        elif cmd[10:-1] == ctrCmd[10]:
            print("Door can be open now!!!!!!")
            Doorlock.opendoor()
        elif cmd[10:-1] == ctrCmd[8]:
            os.system(
                "raspivid -o - -t 0 -hf -w 800 -h 400 -fps 24 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:1235}' :demux=h264 &")
        elif cmd[10:-1] == ctrCmd[9]:
            print(data)
            os.system("pkill raspivid")

    except KeyboardInterrupt:
        GPIO.cleanup()

tcpSerSock.close()
