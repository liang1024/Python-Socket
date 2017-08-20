# coding=utf-8
#UDP发送
import  socket

# 1.创建套接字
udpSocket =  socket.socket( socket.AF_INET,  socket.SOCK_DGRAM)

#2. 绑定本地的相关信息，如果一个网络程序不绑定，则系统会随机分配
bindAddr = ('', 8889) # ip地址和端口号，ip一般不用写，表示本机的任何一个ip
udpSocket.bind(bindAddr)

# 3.准备接收方地址
# sendAddr = ("120.25.233.102", 8888)
sendAddr = ("192.168.31.37", 8888)

# 4.从键盘获取数据
sendData = "Hello,I'm UDP!"

# 5.发送数据到指定的电脑上
udpSocket.sendto(sendData, sendAddr)

# 6.关闭套接字
udpSocket.close()
print("完成了发送")
