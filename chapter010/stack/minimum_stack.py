class MinStack():
    def __init__(self):
        self.main = []
        self.min = []

    def push(self,n):
        if len(self.main) == 0:
            self.min.append(n)
        elif n < self.min[-1]:
            self.min.append(n)
        else:
            self.min.append(self.min[-1])
        self.main.append(n)

    def pop(self):
        self.min.pop()
        return self.main.pop()

    def get_min(self):
        return self.min[-1]


stack = MinStack()
stack.push(3)
stack.push(2)
stack.push(8)
stack.push(1)

print(stack.get_min())      #1
stack.pop()
print(stack.get_min())      #2

# s =[]
# print(s[-1])