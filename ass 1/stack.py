class Stack:
    def __init__(self):
        self.top = None

    def push(self, element):
        if self.top is None:
            self.top = [None, element]
        else:
            self.top = [self.top, element]

    def pop(self):
        temp = self.top[1]
        self.top = self.top[0]
        return temp


s = Stack()
s.push(1)
s.push(2)
s.push(3)
print(s.pop(), s.pop())
