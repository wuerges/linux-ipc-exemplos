from multiprocessing import Process, Lock, Manager

def producer(q):
    for i in range(50):
        print("producing", i)
        q.append(i)

def problematic_consumer(q, i, l):
    for i in range(10):
        while True:
            if len(q) > 0:
                print(i, "consuming", q.pop(0))
                break

def consumer(q, i, l):
    for i in range(10):
        while True:
            with l:
                if len(q) > 0:
                    print(i, "consuming", q.pop(0))
                    break

manager = Manager()
q = manager.list()
l = Lock()

problem = False

p1 = Process(target=producer, args=(q,))
if problem:
    ps = [Process(target=problematic_consumer, args=(q,i, l)) for i in range(5)]
else:
    ps = [Process(target=consumer, args=(q,i, l)) for i in range(5)]

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
