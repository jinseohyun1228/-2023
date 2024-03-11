import sys
from collections import deque

q = deque([])
re = ""

n = int(sys.stdin.readline())

for j in range(n):
    i = sys.stdin.readline().split()

    if i[0] == "push":
        q.append(int(i[1]))
    elif i[0] == "pop":
        if len(q) == 0:
            print(-1)
        else:
            print(q.popleft())
    elif i[0] == "size":
        print(len(q))
    elif i[0] == "empty":
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif i[0] == "front":
        if len(q) == 0:
            print(-1)
        else:
            print(q[0])
    else:
        if len(q)== 0:
            print(-1)
        else:
            print(q[-1])



