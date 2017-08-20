#coding=utf-8
#创建tcp和udp的socket
import socket
def createUDP():
    s= socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    print("创建了UDP")

def createTCP():
    s= socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    print("创建了TCP")

if __name__ == '__main__':
    createTCP()
    createUDP()