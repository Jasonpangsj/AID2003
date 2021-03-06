"""
练习2： 有两个线程同时运行，一个线程打印1--52这52个数字，另外一个线程打印A-Z这26个字母
要求打印出来的顺序是 12A34B56C...5152Z
"""
from threading import Thread, Lock

lock1 = Lock()
lock2 = Lock()


def print_num():
    for i in range(1, 53, 2):
        lock1.acquire()
        print(i)
        print(i + 1)
        lock2.release()


def print_chr():
    for i in range(65, 91):
        lock2.acquire()
        print(chr(i))
        lock1.release()


t1 = Thread(target=print_num)
t2 = Thread(target=print_chr)
lock2.acquire()
t1.start()
t2.start()
t1.join()
t2.join()
