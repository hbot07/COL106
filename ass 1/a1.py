class Stack:
    """
    Stack implementation using LinkedList concept
    O(1) complexity for both push and pop
    """

    def __init__(self):
        self.top = None

    def push(self, element):
        """
        pushes an element to the stack
        :param element: the element to be added to the stack
        :return: Nothing
        """
        if self.top is None:
            self.top = [None, element]
        else:
            self.top = [self.top, element]

    def pop(self):
        """
        removes and returns the element at the top of the stack
        :return: stack element
        """
        temp = self.top[1]
        self.top = self.top[0]
        return temp


operators = {"+", "-"}
digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}


def multiply(list0, multiplier):
    """
    multiplies each element of the list of size 4 by the specified multiplier
    :param list0: list operand
    :param multiplier: multiplier operand
    :return: product result
    """
    return [list0[0] * multiplier, list0[1] * multiplier,
            list0[2] * multiplier, list0[3] * multiplier]


def add(list1, list2):
    """
    add the elements one by one in 2 lists of size 4
    :param list1: operand 1
    :param list2: operand 2
    :return: result sum
    """
    return [list1[0] + list2[0], list1[1] + list2[1],
            list1[2] + list2[2], list1[3] + list2[3]]


def findPositionandDistance(P):
    """
    finding final position and total distance travelled
    :param P: string input
    :return: list [x, y, z, d] specifying the final coordinates and total distance travelled
    """
    number = ""
    command_nest = Stack()
    delta = [0, 0, 0, 0]
    command_nest.push([1, [0, 0, 0, 0]])

    for i in range(len(P)):
        if P[i] in digits:
            number = "".join([number, P[i]])  # efficient method of concatenation?

        # There will always be a number before an opening bracket
        if P[i] == '(':
            command_nest.push([int(number), [0, 0, 0, 0]])
            number = ""

        # code to process elemental steps along x, y, and z axes
        if P[i] in operators:
            delta[3] += 1
            if P[i] == "+":
                if P[i + 1] == "X":
                    delta[0] += 1
                if P[i + 1] == "Y":
                    delta[1] += 1
                if P[i + 1] == "Z":
                    delta[2] += 1
            if P[i] == "-":
                if P[i + 1] == "X":
                    delta[0] -= 1
                if P[i + 1] == "Y":
                    delta[1] -= 1
                if P[i + 1] == "Z":
                    delta[2] -= 1

            temp = command_nest.pop()
            command_nest.push([temp[0], add(temp[1], delta)])
            delta = [0, 0, 0, 0]

        # whenever a closing bracket is found, compute
        if P[i] == ')':
            temp = command_nest.pop()
            temp1 = command_nest.pop()
            temp1 = [temp1[0], add(temp1[1], multiply(temp[1], temp[0]))]
            command_nest.push(temp1)

    return add(command_nest.pop()[1], delta)
