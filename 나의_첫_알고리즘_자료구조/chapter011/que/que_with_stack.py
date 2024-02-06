class Queue:
    def __init__(self):
        self.s1 =[]
        self.s2 =[]
    def enqueue(self,item):
        self.s1.append(item)
    def dequeue(self):
        if len(self.s1) == 0:
            return None
        while len(self.s1) > 1:
            self.s2.append(self.s1.pop())
        re =  self.s1.pop()
        while len(self.s2) != 0 :
            self.s1.append(self.s2.pop())
        return re

q = Queue()


q.enqueue(4)
q.enqueue(3)
q.enqueue(2)

print(q.dequeue())
print(q.dequeue())
print(q.dequeue())
print(q.dequeue())