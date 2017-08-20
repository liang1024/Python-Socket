#coding=utf-8
#TCP服务端
from socket import *

#1.创建socket
tcpServerSocket=socket(AF_INET,SOCK_STREAM)

#2.绑定本地信息
address=('',7788)
tcpServerSocket.bind(address=address)

#3.使用socket创建的套接字默认的属性是主动的，使用listen将其变被动的，这样就可以接收别人的链接了
tcpServerSocket.listen(5)

#4. 如果有新的客户端来链接服务器，那么就产生一个新的套接字专门为这个客户端服务器
# newSocket用来为这个客户端服务
# tcpSerSocket就可以省下来专门等待其他新客户端的链接
newSocket,clientAddr=tcpServerSocket.accept()

#5. 接收对方发送过来的数据，最大接收1024个字节
recvData=newSocket.recv(1024)
print("接收到的数据为：",recvData)

# 6.发送一些数据到客户端
newSocket.send("Thank you!")

# 7.关闭为这个客户端服务的套接字，只要关闭了，就意味着为不能再为这个客户端服务了，如果还需要服务，只能再次重新连接
newSocket.close()

# 8.关闭监听套接字，只要这个套接字关闭了，就意味着整个程序不能再接收任何新的客户端的连接
tcpServerSocket.close()
