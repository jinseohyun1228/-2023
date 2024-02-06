class Node:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next
class LinkedListCycle:
    def __init__(self,num):
        self.head = None
        current = None
        for i in range(1,num+1):
            if self.head is None:
                self.head = Node(i)
                current = self.head
            else:
                current.next = Node(i)
                current = current.next
        current.next = self.head
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

    def josephus_permutation(self,target):
        re = "<"
        current = self.head
        pre = current
        while pre.next is not self.head:
            pre = pre.next
        i = 1
        while current is not None:
            if i == target:
                i = 1
                if current.next is current:
                    re += str(current.data) +">"
                    current = None
                    return re
                pre.next = current.next
                re += str(current.data) + ", "
            else:
                i += 1
                pre = current
            current = current.next
        return re

x_list = [int(i) for i in input().split(" ")]

a_list = LinkedListCycle(x_list[0])
str = a_list.josephus_permutation(x_list[-1])

print(str)




