class BinaryTree:
    def __init__(self,value):
        self.key = value
        self.left_child = None
        self.right_child = None
    def insert_left(self,value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree
    def insert_right(self,value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def breadth_first_search(self,n):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.key == n:
                    return True
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            current = next
            next = []
        return  False

    def find(self,n):
        current = [self]
        next = []
        while current:
            for node in current:
                if node.key == n:
                    return node
                if node.left_child:
                    next.append(node.left_child)
                if node.right_child:
                    next.append(node.right_child)
            current = next
            next = []
        return  False
    def dislocation_movement(self,n):
        current = self
        if current.key == n:
            return True
        elif current.right_child:
            if current.right_child.dislocation_movement(n):
                return True
        elif current.left_child:
            if current.left_child.dislocation_movement(n):
                return True
        return False

def print_pre(current):
    if current:
        if current.key:
            print(current.key ,end=", ")
        if current.right_child:
            print_pre(current.right_child)
        if current.left_child:
            print_pre(current.left_child)
def print_post(current):
    if current:
        if current.left_child:
            print_post(current.left_child)
        if current.right_child:
            print_post(current.right_child)
        if current.key:
            print(current.key ,end=", ")

def print_in(current):
    if current:
        if current.left_child:
            print_in(current.left_child)
        if current.key:
            print(current.key ,end=", ")
        if current.right_child:
            print_in(current.right_child)



tree = BinaryTree(1)
tree.insert_left(2)
tree.find(2).insert_left(3)
tree.find(2).insert_right(4)
tree.find(4).insert_left(5)
tree.find(4).insert_right(6)
tree.insert_right(7)
tree.find(7).insert_left(8)
tree.find(7).insert_right(9)
tree.find(9).insert_left(10)

print("전위이동")
print_pre(tree)
print()
print("후위이동")
print_post(tree)
print()
print("중위이동")
print_in(tree)         # 3 2 1 5 4 6 8 7 9 10
