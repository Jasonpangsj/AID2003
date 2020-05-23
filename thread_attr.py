from threading import Thread
from time import sleep

def fun():
    sleep(3)
    print("线程属性测试")


t = Thread(target=fun)



#t.setDaemon(True)
t.start()
t.setName("Tedu")
print("is_alive",t.is_alive())
print("线程名称:",t.getName())