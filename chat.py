import socket
import threading as thd
import os

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
localIP = input("Enter Your IP: ")
s.bind((localIP, 143))

usrIP = input("Enter Partner IP: ")
print()

def recv_msg():
    while True:
        msgRcv = s.recvfrom(1024)
        if msgRcv[0].decode() == "quit":
            print("Partner is Offline!")
            os._exit(1)
        print(msgRcv[1][0] + ": " + msgRcv[0].decode())

def send_msg():
    while True:
        data = input().encode()
        msgSent = s.sendto(data, (usrIP, 143))
        if data.decode() == "quit":
            os._exit(1)

send_thd = thd.Thread(target=send_msg)
rcv_thd = thd.Thread(target=recv_msg)

send_thd.start()
rcv_thd.start()
