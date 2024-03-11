class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class Stack_linked_list:
    def __init__(self):
        self.head = None

    def method01(self, data):
        if self.head is None:
            self.head = Node(data)
        else:
            new = Node(data)
            new.next = self.head
            self.head = new

    def method02(self):
        if self.head is None:
            return "-1"
        re = self.head.data
        self.head = self.head.next
        return str(re)

    def method03(self):
        i = 0
        current = self.head
        while current is not None:
            i += 1
            current = current.next
        return str(i)

    def method04(self):
        if self.head is None:
            return "1"
        else:
            return "0"

    def method05(self):
        if self.head is not None:
            return str(self.head.data)
        else:
            return "-1"


import sys

stack = Stack_linked_list()
re = ""
j = 1

n = int(sys.stdin.readline())

for h in range(n):
    i = sys.stdin.readline().split()

    if i[0] == "1":
        stack.method01(int(i[-1]))
    elif i[0] == "2":
        re += stack.method02()
    elif i[0] == "3":
        re += stack.method03()
    elif i[0] == "4":
        re += stack.method04()
    else:
        re += stack.method05()
    if i[0] != "1" and j != n:
        re += "\n"
    j+=1

print(re)
