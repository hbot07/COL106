from avl_tree import AVLTree


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


# points = [(1, 6), (2, 4), (3, 7), (4, 9), (5, 1), (6, 3), (7, 8), (8, 10), (9, 2), (10, 5)]
# # for i in range(10):
# #     pointDbObject = PointDatabase(points[:i])
# #     print("x", [i.point for i in pointDbObject.x.in_order(pointDbObject.x.root)])
# #     print("y", [i.point for i in pointDbObject.y.in_order(pointDbObject.y.root)])
#
# pointsy = [Point(i, 'y') for i in points]
# yt = AVLTree()
# for i in pointsy[:5]:
#     yt.insert(i)
# print([j.point for j in yt.in_order(yt.root)], [j.point for j in yt.pre_order(yt.root)])
# yt.insert(Point((6, 3), 'y'))
# print([j.point for j in yt.in_order(yt.root)], [j.point for j in yt.pre_order(yt.root)])

pointDbObject = PointDatabase([(1, 6), (2, 4), (3, 7), (4, 9), (5, 1), (6, 3), (7, 8), (8, 10),
                               (9, 2), (10, 5)])
print(pointDbObject.searchNearby((5, 5), 1),
      pointDbObject.searchNearby((4, 8), 2),
      pointDbObject.searchNearby((10, 2), 1.5), sep="\n")
