import os
import RoomLight          # import RoomLight.py as a library
import Window             # import Window.py as a library
from socket import *      # import every function in socket library
import RPi.GPIO as GPIO   # import Raspberry Pi GPIO library as GPIO
import DoorLock           # import Doorlock.py as a library

RoomLight.setup()         # run RoomLight setup function
Window.setup()            # run Window setup function
DoorLock.setup()          # run Doorlock setup function

ctrCmd = ['1true', '1false', '2true', '2false', '3true',
          '3false', 'wtrue', 'wfalse', 'v', 'vt', 'd']      # store the commands sent from MyHome application

HOST = '192.168.43.5'
PORT = 1234
BUFSIZE = 1024
ADDR = (HOST, PORT)      # setup socket server information (IP address, port number and size of the package)

tcpSerSock = socket(AF_INET, SOCK_STREAM)  # Build a Socket based on TCP connection
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)                       # Server start to listen up to 4 client request

while True:
    print('Waiting for connection')
    conn, addr = tcpSerSock.accept()      # accept the request from client and build connection
    print('...connected from :', addr)

    try:
        data = conn.recv(BUFSIZE)         # receive and data send from client and check the command within the while loop
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
            DoorLock.opendoor()
        elif cmd[10:-1] == ctrCmd[8]:
            os.system(
                "raspivid -o - -t 0 -hf -w 800 -h 400 -fps 24 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:1235}' :demux=h264 &")  # start the camera and stream to the destination at port 1235
        elif cmd[10:-1] == ctrCmd[9]:
            print(data)
            os.system("pkill raspivid")  # stop camera streaming

    except KeyboardInterrupt:
        GPIO.cleanup()   # initiate all GPIO
