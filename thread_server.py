from socket import *
from threading import Thread

HOST = "0.0.0.0"
PORT = 9999
ADDR = (HOST, PORT)


# 处理客户端的具体请求 子进程函数
def handle(connfd):
    while True:
        data = connfd.recv(1024)
        if not data:
            break
        print(data.decode())
        connfd.send(b'OK')
    connfd.close()


# 创建tcp套接字
sockfd = socket()
sockfd.bind(ADDR)
sockfd.listen(5)


print("Listen the port %d"%PORT)
# 循环处理客户端链接
while True:
    try:
        connfd,addr = sockfd.accept()
        print("Connect from",addr)
    except KeyboardInterrupt:
        print("服务结束")
        break

    # 为客户端创建进程
    t = Thread(target = handle,args = (connfd,))
    t.setDaemon(True)  # 子进程随父进程退出
    t.start()


sockfd.close()
