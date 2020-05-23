from socket import *

ADDR = ("127.0.0.1",9999)

class FtpClient():
    def __init__(self, sockfd):
        self.sockfd =sockfd

    def do_list(self):
        self.sockfd.send(b"L")
        data = self.sockfd.recv(128).decode()
        if data == "OK":
            data = self.sockfd.recv(1024*1024)
            print(data.decode())
        else:
            print("文件夹为空")


def main():
    sockfd = socket()
    sockfd.connect(ADDR)

    ftp = FtpClient(sockfd)

    while True:
        print("=================命令选项====================")
        print("*****            list               *****")
        print("*****          get file             *****")
        print("*****          put file             *****")
        print("*****            quit               *****")
        print("============================================")
        cmd = input("请输入命令")

        if cmd == "list":
            ftp.do_list()
        if cmd == "get":
            file_name =


if __name__ == '__main__':
    main()