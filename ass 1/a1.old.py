class Stack:
    def __init__(self):
        self.data = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()


operators = {"+", "-"}
axis = {"X", "Y", "Z"}
digits = {"0", "1", "2", "3", "4", "5", "6", "7", "8", "9"}
brackets = {"(", ")"}


def correspondingBracketIndex(P, i):
    counter = 0
    while True:
        if P[i] == '(':
            counter += 1
        if P[i] == ")":
            counter -= 1

        if counter == 0:
            return i

        i += 1


def numberBefore(P, indexOfBracket):
    start = indexOfBracket - 1
    while True:
        if not (P[start] in digits):
            break
        start -= 1
    return int(P[start + 1: indexOfBracket])


def add(list1, list2):
    return [list1[0] + list2[0], list1[1] + list2[1], list1[2] + list2[2], list1[3] + list2[3]]


def multiply(list0, multiplier):
    return [list0[0] * multiplier, list0[1] * multiplier,
            list0[2] * multiplier, list0[3] * multiplier]


def findPositionandDistance_helper(P):
    delta = [0, 0, 0, 0]

    i = 0
    while i < len(P):
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
        if P[i] == "(":
            end = correspondingBracketIndex(P, i)
            delta = add(delta, multiply(findPositionandDistance_helper(P[i + 1:end]), numberBefore(P, i)))
            i = end
        i += 1

    return delta


def findPositionandDistance(P):
    return findPositionandDistance_helper(P)


# print(findPositionandDistance_helper("5(+X+Y-Z)+X+Z5(+X)"))
# print(findPositionandDistance_helper("+X+X+X+X+X-X-X-X-X-X-X-X-X-X-X"))
# print(correspondingBracketIndex("()))", 0))
# print(numberBefore("123(643(5(", 7))
# print(findPositionandDistance_helper("1(+X)5(+Y)41(+Z)1805(-X)3263441(-Y)10650056950805(-Z)"))
# print(findPositionandDistance('1(+X)5(+Y)41(+Z)1805(-X)3263441(-Y)10650056950805(-Z)'))
