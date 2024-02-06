import sys

n = int(sys.stdin.readline())
n_set = set(map(int, input().split()))

m = int(sys.stdin.readline())
m_set = list(map(int, input().split()))

str = []
for i in m_set:
    if i in n_set:
        str.append(1)
    else:
        str.append(0)

for i in str:
    print(i)