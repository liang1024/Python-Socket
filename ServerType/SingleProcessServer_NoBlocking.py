#coding=utf-8
#单进程服务器，无阻塞版
from socket import *
import time

# 用来存储所有的新链接的socket
g_socketList = []

def main():
    serSocket = socket(AF_INET, SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR  , 1)
    localAddr = ('', 7788)
    serSocket.bind(localAddr)
    #可以适当修改listen中的值来看看不同的现象
    serSocket.listen(1000)
    #将套接字设置为非堵塞
    #设置为非堵塞后，如果accept时，恰巧没有客户端connect，那么accept会
    #产生一个异常，所以需要try来进行处理
    serSocket.setblocking(False)

    while True:

        #用来测试
        #time.sleep(0.5)

        try:
            newClientInfo = serSocket.accept()
        except Exception as result:
            pass
        else:
            print("一个新的客户端到来:%s"%str(newClientInfo))
            newClientInfo[0].setblocking(False)
            g_socketList.append(newClientInfo)

        # 用来存储需要删除的客户端信息
        needDelClientInfoList = []

        for clientSocket,clientAddr in g_socketList:
            try:
                recvData = clientSocket.recv(1024)
                if len(recvData)>0:
                    print('recv[%s]:%s'%(str(clientAddr), recvData))
                else:
                    print('[%s]客户端已经关闭'%str(clientAddr))
                    clientSocket.close()
                    needDelClientInfoList.append((clientSocket,clientAddr))
            except Exception as result:
                pass

        for needDelClientInfo in needDelClientInfoList:
            g_socketList.remove(needDelClientInfo)

if __name__ == '__main__':
    main()

