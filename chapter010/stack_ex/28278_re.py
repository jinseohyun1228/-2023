import sys

stack = []

n = int(sys.stdin.readline())

for h in range(n):
    i = sys.stdin.readline().split()
    if i[0] == "1":
        stack.append(int(i[1]))
    elif i[0] == "2":
        if len(stack) == 0:
            print("-1")
        else:
            print(stack.pop())
    elif i[0] == "3":
        print(len(stack))
    elif i[0] == "4":
        if len(stack) == 0:
            print("1")
        else:
            print(0)
    else:
        if len(stack) == 0:
            print("-1")
        else:
            print(stack[-1])
