class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.isLeaf = False
        self.leaves = []
        self.index = None

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        self.key = str(self.data) + ', ' + str(self.leaves)
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


class RangeTree:
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
            temp.leaves = elements[left:right+1]
            return temp

    def search(self, lower, upper):
        return self.search_helper(self.root, lower, upper)

    def search_helper(self, root, lower, upper):
        if root is None:
            return []
        low, high = root.leaves[0], root.leaves[-1]
        if lower <= low and upper >= high:
            return root.leaves
        else:
            return self.search_helper(root.left, lower, upper) + self.search_helper(root.right, lower, upper)


tree1 = RangeTree([i for i in range(0, 64, 4)])
tree1.root.display()
print(tree1.search(5, 40))
