#coding=utf-8
#UDP接收
import  socket

# 1.创建UDP
udpSocket=  socket.socket( socket.AF_INET,  socket.SOCK_DGRAM)

#2.绑定本地ip,端口
bindAddr=('',8888) # ip,端口，默认为本机ip
udpSocket.bind(bindAddr)

# 3.等待接收方发送的数据 阻塞式
recvData=udpSocket.recvfrom(1024) #每次接收1024个字节

# 4.显示接收的数据
print(recvData)

#5关闭套接字
udpSocket.close()