from multiprocessing import Process, Queue
import time


def producer(q):
    for i in range(10):
        time.sleep(1)
        print("producing", i)
        q.put(i)

def consumer(q):
    for i in range(10):
        print("consuming", q.get())



q = Queue()

p1 = Process(target=producer, args=(q,))
p2 = Process(target=consumer, args=(q,))

p1.start()
p2.start()
p1.join()
p2.join()

print("OK")
