import signal, time


def handler(signum, frame):
    print("Received {} {}".format(signum, frame))
    if(signum == signal.SIGALRM):
        signal.alarm(5)


signal.signal(signal.SIGALRM, handler)
signal.alarm(5)

while True:
    print("sleeping 10")
    time.sleep(1)


