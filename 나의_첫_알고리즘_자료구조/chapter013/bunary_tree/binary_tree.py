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

    def print_pre(self):
        current = self
        if current.key:
            print(current.key ,end=", ")
        elif current.right_child:
            current.right_child.print_pre()
        elif current.left_child:
            current.left_child.print_pre()
        print()
    def print_post(self):
        current = self
        if current.left_child:
            current.left_child.print_post()
        elif current.right_child:
            current.right_child.print_post()
        elif current.key:
            print(current.key ,end=", ")
        print()
    def print_in(self):
        current = self
        if current.left_child:
            current.left_child.print_pre()
        elif current.key:
            print(current.key ,end=", ")
        elif current.right_child:
            current.right_child.print_pre()
        print()


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

tree.print_pre()        # 1 3 4 5 6 7 8 9 10
tree.print_post()       # 3 5 6 4 2 8 10 9 7 1
tree.print_in()         # 3 2 1 5 4 6 8 7 9 10
