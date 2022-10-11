class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.isLeaf = False
        self.leaves = []
        self.index = None
        self.aux_tree = None


class AuxTree:
    def __init__(self, elements):
        self.elements = elements.copy()
        self.elements.sort()
        self.root = self.construct(self.elements, 0, len(self.elements) - 1)

    def construct(self, elements, left, right):
        if left > right:
            return None
        if left == right:
            temp = Node(elements[left])
            temp.isLeaf = True
            temp.index = left
            temp.leaves = [elements[left]]
            return temp
        else:
            mid = (left + right) // 2
            temp = Node(elements[mid])
            temp.left = self.construct(elements, left, mid)
            temp.right = self.construct(elements, mid + 1, right)
            temp.leaves = elements[left:right + 1]
            return temp

    def search(self, lower, upper):
        return self.search_helper(self.root, lower, upper)

    def search_helper(self, root, lower, upper):
        if root is None:
            return []
        low, high = root.leaves[0].value, root.leaves[-1].value
        if lower <= low and upper >= high:
            return root.leaves
        else:
            return self.search_helper(root.left, lower, upper) + self.search_helper(root.right, lower, upper)


class RangeTree:
    def __init__(self, elements):
        self.elements = elements.copy()
        self.elements.sort()
        self.root = self.construct(self.elements, 0, len(self.elements) - 1)
        self.construct2(self.root)

    def construct2(self, root):
        if root is None:
            return
        root.aux_tree = AuxTree([Point(i.point, 'y') for i in root.leaves])
        self.construct2(root.left)
        self.construct2(root.right)

    def construct(self, elements, left, right):
        if left > right:
            return None
        if left == right:
            temp = Node(elements[left])
            temp.isLeaf = True
            temp.index = left
            temp.leaves = [elements[left]]
            return temp
        else:
            mid = (left + right) // 2
            temp = Node(elements[mid])
            temp.left = self.construct(elements, left, mid)
            temp.right = self.construct(elements, mid + 1, right)
            temp.leaves = elements[left:right + 1]
            return temp

    def search(self, lower_x, upper_x, lower_y, upper_y):
        return self.search_helper(self.root, lower_x, upper_x, lower_y, upper_y)

    def search_helper(self, root, lower_x, upper_x, lower_y, upper_y):
        if root is None:
            return []
        low, high = root.leaves[0].value, root.leaves[-1].value
        if lower_x <= low and upper_x >= high:
            return root.aux_tree.search(lower_y, upper_y)
        else:
            return self.search_helper(root.left, lower_x, upper_x, lower_y, upper_y) + \
                   self.search_helper(root.right, lower_x, upper_x, lower_y, upper_y)


class Point:
    def __init__(self, point, cmp='x'):
        self.point = point
        if cmp == 'x':
            self.value = point[0]
        else:
            self.value = point[1]

    def __lt__(self, other):
        return self.value < other.value

    def __le__(self, other):
        return self.value <= other.value

    def __eq__(self, other):
        return self.value == other.value

    def __ne__(self, other):
        return self.value != other.value

    def __gt__(self, other):
        return self.value > other.value

    def __ge__(self, other):
        return self.value >= other.value


class PointDatabase:
    def __init__(self, pointlist):
        self.tree = RangeTree([Point(i, 'x') for i in pointlist])

    def searchNearby(self, q, d):
        return [i.point for i in self.tree.search(q[0] - d, q[0] + d, q[1] - d, q[1] + d)]
