import mmap
import os

mm = mmap.mmap(-1, 13)
pid = os.fork()

mm.write(b"Hello world!")

mm.seek(0)
print("pid:", pid, "read:", mm.readline())
mm.close()
