#coding=utf-8
#TCP客户端
from socket import *

# 1.创建socket
tcpClientSocket=socket(AF_INET,SOCK_STREAM)

# 2.链接到服务器
serverAddr=('192.168.1.2',7788)
tcpClientSocket.connect(serverAddr)

# 3.输入数据
sendData="I'm Client!"
tcpClientSocket.send(sendData)

# 4.接收对方发送过来的数据，最大接受1024字节
recvData=tcpClientSocket.recv(1024)
print("接收到的数据为：",recvData)

# 5.关闭套接字
tcpClientSocket.close()
