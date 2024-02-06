class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkedListCycle:
    def __init__(self):
        self.head = None
    def append(self,data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head  #환형
            return
        current = self.head
        while current.next != self.head:    #환형의 마지막 부분 찾기
            current = current.next
        last = Node(data)
        last.next = self.head
        current.next = last            #마지막 부분 환형으로 만들기

    def __str__(self):
        re = ""
        node = self.head
        if node is not None:
            re += str(node.data) +" "
            node = node.next
        while node is not self.head:
            re += str(node.data) +" "
            node = node.next
        return re

    def serch(self,target):
        current = self.head
        if current is None:
            return False
        if current.data == target:
            return True
        current = current.next
        while current is not self.head:
            if current.data == target:
                return True
            current = current.next
        return False

    def removeAll(self,target):
        while self.head.data is target:
            if self.head.next == self.head:
                self.head = None
                return
            else:
                self.head = self.head.next
        currnet = self.head.next
        pre = self.head
        while currnet != self.head:
            if currnet.data == target:
                pre.next = currnet.next
            else:
                pre = currnet
            currnet = currnet.next

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


a_lsit = LinkedListCycle()
a_lsit.append(3)
a_lsit.append(3)
a_lsit.append(1)
a_lsit.append(2)
a_lsit.append(3)
a_lsit.append(3)
a_lsit.append(3)
a_lsit.append(4)
a_lsit.append(1)
a_lsit.append(3)
a_lsit.append(3)

print(a_lsit)
a_lsit.removeAll(3)
print(a_lsit)
print(a_lsit.detect_cycle())

for i in range(1,3):
    print(i)