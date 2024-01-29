class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self,data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def __str__(self):
        re = ""
        node = self.head
        while node is not None:
            re += str(node.data) +" "
            node = node.next
        return re

    def serch(self,target):
        current = self.head
        if current is None:
            return False
        while current is not None:
            if current.data == target:
                return True
            current = current.next
        return False

    def removeAll(self,target):
        while self.head.data is target:
            self.head = self.head.next
        currnet = self.head.next
        pre = self.head
        while currnet:
            if currnet.data == target:
                pre.next = currnet.next
            else:
                pre = currnet
            currnet = currnet.next

    def reverse_list(self):
        current = self.head
        previous = None
        while current: #지금
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except:
                return False



a_lsit = LinkedList()
a_lsit.append(3)
a_lsit.append(4)
a_lsit.append(5)
a_lsit.append(7)
a_lsit.append(3)
a_lsit.append(3)
a_lsit.append(4)
a_lsit.append(4)
a_lsit.append(1)

print(a_lsit.serch(8)) #False
print(a_lsit.serch(4)) #True

print(a_lsit)
a_lsit.removeAll(3)
print(a_lsit)

a_lsit.reverse_list()

print(a_lsit)

print(a_lsit.detect_cycle())


