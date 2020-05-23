from threading import Thread
from time import sleep

ticket = ["T%d" % x for x in range(1, 501)]


def sell(w):
    while ticket:
        try:
            sleep(0.1)
            print("%s窗口出售:%s" % (w, ticket.pop(0)))
        except:
            print("票已售空")


jobs = []
for i in range(1, 11):
    t = Thread(target=sell, args=("W%d" % i,))
    jobs.append(t)
    t.start()

for i in jobs:
    i.join()
