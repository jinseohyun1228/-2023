# 이진 힙
'''
class Binary_heap:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = Binary_heap(value)
        else:
            bin_tree = Binary_heap(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = Binary_heap(value)
        else:
            bin_tree = Binary_heap(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def insert_empty(self, value):
        current = [self]
        next = []
        if current:
            if current.left_child is None:
                current.left_child = self.
                return
            current.left_child.insert_empty(value)
            if current.right_child is None:
                current.right_child = Binary_heap(value)
                return
            current.right_child.insert_empty(value)


def print_post(current):
    if current:
        if current.left_child:
            print_post(current.left_child)
        if current.right_child:
            print_post(current.right_child)
        if current.key:
            print(current.key, end=", ")


tree = Binary_heap(1)
Binary_heap.insert_empty()

print_post(tree)
'''