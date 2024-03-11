class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Que:
    def __init__(self):
        self.front = None
        self.rear = None
        self._size = 0

    def enqueue(self,item):
        self._size += 1
        if self.front is None:
            self.front = Node(item)
            return
        if self.rear is None:
            self.rear = Node(item)
            self.front.next = self.rear
            return
        node = Node(item)
        self.rear.next = node
        self.rear = node
        return

    def dequeue(self):
        if self.front is None:
            self._size += -1
            return None
        re = self.front
        self.front = self.front.next
        if self.front is not None:
            self._size += -1
        return re.data
    def size(self):
        return self._size
    def __str__(self):
        re = ""
        current = self.front
        if current is None:
            return re
        while current is not self.rear:
            re += str(current.data) + " "
            current = current.next
        re += str(current.data) + " "
        return re

a = Que()
a.enqueue(4)
a.enqueue(2)
a.enqueue(1)
a.enqueue(3)

print(a)

print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())
print(a.dequeue())

print(a.size())