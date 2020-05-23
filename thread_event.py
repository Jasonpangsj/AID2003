from threading import Event, Thread

message = None
e = Event()


def yzr():
    print("yzr前来拜山头")
    global message
    message = "天王盖地虎"
    e.set()


t = Thread(target=yzr)
t.start()

e.wait()
print("说对口令就是对的人")

if message == "天王盖地虎":
    print("宝塔镇河妖")
    print("确认过眼神,你是对的人")
else:
    print("打死他,不用给面子")
