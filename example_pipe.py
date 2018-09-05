from subprocess import Popen, PIPE
import sys

with Popen(["cat"], stdout=PIPE, stdin=sys.stdin) as x:
    print(x.communicate())
