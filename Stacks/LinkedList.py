class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, element):
        if self.head is None:
            self.head = [None, None, element]
            self.tail = self.head
        else:
            self.tail[0], self.tail[1], self.tail[2] = self.tail, None, element

    def pop(self):
        temp = self.tail[2]
        self.tail[0], self.tail[1], self.tail[2] = self.tail[0][0], None, self.tail[0][2]
        return temp


l = LinkedList()
l.append(1)
l.append(2)
l.append(3)
print(l.pop())
print(l.pop())
