from threading import Thread
import time

class MyThread(Thread):
    def __init__(self, sec, song):
        self.sec = sec
        self.song = song
        super().__init__()

    def run(self):
        for i in range(3):
            print("Playing %s %s"%(self.song,time.ctime()))
            time.sleep(self.sec)

t=MyThread(2,"下山")
t.start()
t.join()