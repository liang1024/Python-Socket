#coding=utf-8
#单进程服务器
from socket import *

serSocket = socket(AF_INET, SOCK_STREAM)

# 重复使用绑定的信息
serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR  , 1)

localAddr = ('', 7788)

serSocket.bind(localAddr)

serSocket.listen(5)

while True:

    print('-----主进程，，等待新客户端的到来------')

    newSocket,destAddr = serSocket.accept()

    print('-----主进程，，接下来负责数据处理[%s]-----'%str(destAddr))

    try:
        while True:
            recvData = newSocket.recv(1024)
            if len(recvData)>0:
                print('recv[%s]:%s'%(str(destAddr), recvData))
            else:
                print('[%s]客户端已经关闭'%str(destAddr))
                break
    finally:
        newSocket.close()

serSocket.close()

'''
总结
同一时刻只能为一个客户进行服务，不能同时为多个客户服务
类似于找一个“明星”签字一样，客户需要耐心等待才可以获取到服务
当服务器为一个客户端服务时，而另外的客户端发起了connect，只要服务器listen的队列有空闲的位置，就会为这个新客户端进行连接，并且客户端可以发送数据，但当服务器为这个新客户端服务时，可能一次性把所有数据接收完毕
当recv接收数据时，返回值为空，即没有返回数据，那么意味着客户端已经调用了close关闭了；因此服务器通过判断recv接收数据是否为空 来判断客户端是否已经下线
'''