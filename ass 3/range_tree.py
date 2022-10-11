class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.isLeaf = False
        self.range = None
        self.index = None
        self.key = self.data

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
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
            return temp
        else:
            mid = (left + right) // 2
            temp = Node(elements[mid])
            temp.left = self.construct(elements, left, mid)
            temp.right = self.construct(elements, mid + 1, right)
            temp.range = (elements[left], elements[right])
            return temp

    def search(self, lower, upper):
        l = self.search_helper(self.root, lower)
        r = self.search_helper(self.root, upper)
        if l.index == r.index:
            if not (lower <= self.elements[l.index] <= upper):
                return None
        return l.index, r.index

    # def search_helper(self, root, lower, upper):
    #     if root.isLeaf:
    #         if lower <= root.data <= upper:
    #             return root.index, root.index
    #     if upper < root.range[0]:
    #         return None
    #     if lower > root.range[1]:
    #         return None
    #     if lower < root.range[0] and upper > root.range[1]:
    #         return 0, len(self.elements) - 1
    #
    #     if lower > root.data:
    #         return self.search_helper(root.left, lower, upper)
    #     else:
    #         if upper <= root.data:
    #             return self.search_helper(root.left, lower, upper)
    #         else:
    #             left_search = self.search_helper(root.left, lower, upper)
    #             right_search = self.search_helper(root.right, lower, upper)
    #             if left_search is None:
    #                 if right_search is None:
    #                     return None
    #                 else:
    #                     left_search = right_search
    #             else:
    #                 if right_search is None:
    #                     right_search = left_search
    #             return left_search[0], right_search[1]

    def search_helper(self, root, value):
        if root.isLeaf:
            return root

        if root.data >= value:
            return self.search_helper(root.left, value)
        else:
            return self.search_helper(root.right, value)


tree1 = RangeTree([i for i in range(16)])
tree1.root.display()
print(tree1.search(100, 100))
