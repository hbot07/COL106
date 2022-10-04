class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def __len__(self):
        return len(self.data)


def isValid(s: str) -> bool:
    S = Stack()
    valid = True
    for i in s:
        if i in {'(', '[', '{'}:
            S.push(i)
            continue

        if i == ')':
            valid = S.pop() == '('
        if i == '}':
            valid = S.pop() == '{'
        if i == ']':
            valid = S.pop() == '['

        if not valid:
            return False

    if len(S) != 0:
        return False

    return True
