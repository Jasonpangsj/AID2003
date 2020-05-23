"""
ftp文件服务器
"""
from socket import *
from threading import Thread
import os
from time import sleep

HOST = "0.0.0.0"
PORT = 9999
ADDR = (HOST, PORT)
FTP = "/home/tarena/ftp"


class FtpServer(Thread):
    def __init__(self, connfd):
        self.connfd = connfd
        super().__init__()

    def do_list(self):
        file_list = os.listdir(FTP)
        if not file_list:
            self.connfd.send(b"Fail")
            return
        else:
            self.connfd.send(b"OK")
            sleep(0.1)
            files = "\n".join(file_list)
            self.connfd.send(files.encode())

    def do_get(self):
        try:
            f = open(FTP+filename,"rb")
        except:
            self.connfd.send(b"Fail")
        else:
            self.connfd.send(b"OK")
            sleep(0.1)
            while True:
                data = f.read(1024*10)
                if not data :
                    self.connfd.send(b"##")

    def run(self):
        while True:
            data = self.connfd.recv(1024).decode()
            if data == "L":
                self.do_list()
            elif data[0] == "D":
                self.do_get()


def main():
    # 创建tcp套接字
    sockfd = socket()
    sockfd.bind(ADDR)
    sockfd.listen(5)

    print("Listen the port %d" % PORT)
    # 循环处理客户端链接
    while True:
        try:
            connfd, addr = sockfd.accept()
            print("Connect from", addr)
        except KeyboardInterrupt:
            print("服务结束")
            break

        # 为客户端创建进程
        t = FtpServer(connfd)
        t.setDaemon(True)  # 子进程随父进程退出
        t.start()

    sockfd.close()


if __name__ == '__main__':
    main()
