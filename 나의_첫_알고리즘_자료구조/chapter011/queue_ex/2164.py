from collections import deque

n = int(input())

list = list(range(1,n+1))
q = deque(list)

while len(q) != 1:
    q.popleft()
    q.rotate(-1)

print(q[0])