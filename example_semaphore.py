
from multiprocessing import Process, Lock, Manager, Semaphore

def producer(q):
    for i in range(500):
        print("producing", i)
        q.append(i)

def consumer(q, i, l):
    for i in range(10):
        while True:
            #if True:
            with s:
                x = sum(i for i in range(int(1e5)))
                print("sum ", x)
                with l:
                    if len(q) > 0:
                        print(i, "consuming", q.pop(0))
                        break

manager = Manager()
q = manager.list()
l = Lock()
s = Semaphore(6) # 6 because my machine has 6 cores

p1 = Process(target=producer, args=(q,))
ps = [Process(target=consumer, args=(q,i, l)) for i in range(50)]

p1.start()
for p in ps:
    p.start()

p1.join()
for p in ps:
    p.join()

if q:
    print("ERROR, q is not empty:", q)
else:
    print("OK")
