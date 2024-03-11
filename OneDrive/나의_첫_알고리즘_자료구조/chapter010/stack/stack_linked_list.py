class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class Stack_linked_list:
    def __init__(self):
        self.head = None
    def push(self,data):
        if self.head is None:
            self.head = Node(data)
        else:
            new = Node(data)
            new.next = self.head
            self.head = new

    def pop(self):
        if self.head is None:
            return False
        re = self.head.data
        self.head = self.head.next
        return re

stack = Stack_linked_list()
stack.push(1)
stack.push(3)
stack.push(5)

print(stack.pop())  #5
print(stack.pop())  #3
print(stack.pop())  #1
print(stack.pop())  #False