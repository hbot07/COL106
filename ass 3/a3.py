class Node:
    def __init__(self, left, right, data, parent):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent
        self.height = 0


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, element):
        if self.root is None:
            self.root = Node(None, None, element, None)
            return self.root
        cursor = self.root
        while True:
            if cursor.data > element:
                if cursor.left is None:
                    cursor.left = Node(None, None, element, cursor)
                    return cursor.left
                else:
                    cursor = cursor.left
            else:
                if cursor.right is None:
                    cursor.right = Node(None, None, element, cursor)
                    return cursor.right
                else:
                    cursor = cursor.right

    def in_order(self, root):
        l = []
        self.in_order_helper(root, l)
        return l

    def in_order_helper(self, root, l):
        if root is not None:
            self.in_order_helper(root.left, l)
            l.append(root.data)
            self.in_order_helper(root.right, l)

    def between(self, lower_bound, upper_bound):
        return self.between_helper(self.root, lower_bound, upper_bound)

    def between_helper(self, root, lower_bound, upper_bound):
        if root is None:
            return []
        if root.data > upper_bound:
            return self.between_helper(root.left, lower_bound, upper_bound)
        if root.data < lower_bound:
            return self.between_helper(root.right, lower_bound, upper_bound)

        return self.between_helper(root.left,
                                   lower_bound, upper_bound) + [root.data] + self.between_helper(root.right,
                                                                                                 lower_bound,
                                                                                                 upper_bound)

    def print_tree(self):
        queue = [self.root]
        while len(queue) > 0:
            l = []
            for i in queue:
                print(i.data, end=" ")
                if i.left is not None:
                    l.append(i.left)
                if i.right is not None:
                    l.append(i.right)
            queue = l
            print()


class AVLTree(BinaryTree):
    def get_height(self, node):
        if node is None:
            return 0
        else:
            return node.height

    def insert(self, element):
        inserted = super().insert(element)
        self.update_heights(inserted)
        self.fix_imbalance_insert(inserted)

    def fix_imbalance_insert(self, inserted):
        deepest_unbalanced = self.get_deepest_unbalanced_node(inserted)
        self.fix_imbalance(deepest_unbalanced)

    def fix_imbalance(self, root):
        if root is None:
            return

        if self.get_height(root.left) > self.get_height(root.right):
            if self.get_height(root.left.left) >= self.get_height(root.left.right):
                self.right_rotate(root)
            else:
                self.left_rotate(root.left)
                self.right_rotate(root)
        else:
            if self.get_height(root.right.right) >= self.get_height(root.right.left):
                self.left_rotate(root)
            else:
                self.right_rotate(root.right)
                self.left_rotate(root)

        self.update_heights(root)
        self.update_heights(root.left)
        self.update_heights(root.right)

    def right_rotate(self, root):
        parent = root.parent
        p = root.left
        q = root
        t2 = p.right

        if parent is not None:
            if parent.right is q:
                parent.right = p
            else:
                parent.left = p
        else:
            self.root = p
        p.parent = parent

        q.parent = p
        p.right = q

        q.left = t2
        if t2 is not None:
            t2.parent = q

        q.height = max(self.get_height(q.left), self.get_height(q.right))
        self.update_heights(q)

    def left_rotate(self, root):
        parent = root.parent
        p = root
        q = root.right
        t2 = q.left

        if parent is not None:
            if parent.right is p:
                parent.right = q
            else:
                parent.left = q
        else:
            self.root = q
        q.parent = parent

        p.parent = q
        q.left = p

        p.right = t2
        if t2 is not None:
            t2.parent = p

        p.height = max(self.get_height(p.left) + 1, self.get_height(p.right) + 1)
        self.update_heights(p)

    def get_deepest_unbalanced_node(self, cursor):
        if cursor is None:
            return
        delta_h = self.get_height(cursor.left) - self.get_height(cursor.right)
        if abs(delta_h) > 1:
            return cursor
        return self.get_deepest_unbalanced_node(cursor.parent)

    def update_heights(self, cursor):
        if cursor is None:
            return
        pre = cursor.height
        cursor.height = max(self.get_height(cursor.left) + 1,
                            self.get_height(cursor.right) + 1)
        if cursor.height == pre:
            return
        return self.update_heights(cursor.parent)


class Point:
    def __init__(self, point, cmp):
        self.point = point
        if cmp == 'x':
            self.value = point
        else:
            self.value = point[::-1]

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
        self.x = AVLTree()
        self.y = AVLTree()
        for point in pointlist:
            self.x.insert(Point(point, 'x'))
            self.y.insert(Point(point, 'y'))

    def searchNearby(self, q, d):
        xl = set(i.point for i in self.x.between(Point((q[0] - d, 0), 'x'),
                                                 Point((q[0] + d, 0), 'x')))
        yl = set(i.point for i in self.y.between(Point((0, q[1] - d), 'y'),
                                                 Point((0, q[1] + d), 'y')))
        return list(xl.intersection(yl))


pointDbObject = PointDatabase([(1, 6), (2, 4), (3, 7), (4, 9), (5, 1), (6, 3), (7, 8), (8, 10),
                               (9, 2), (10, 5)])
print(pointDbObject.searchNearby((5, 5), 1),
      pointDbObject.searchNearby((4, 8), 2),
      pointDbObject.searchNearby((10, 2), 1.5), sep="\n")
