import heapq

"""
Min Heap Implementation in Python
"""


class MinHeap:
    def __init__(self):
        """
        On this implementation the heap list is initialized with a value
        """
        self.heap_list = [0]
        self.current_size = 0

    def sift_up(self, i):
        """
        Moves the value up in the tree to maintain the heap property.
        """
        # While the element is not the root or the left element
        Stop = False
        while (i // 2 > 0) and Stop == False:
            # If the element is less than its parent swap the elements
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
                self.heap_list[i][3] = i
                self.heap_list[i // 2][3] = i // 2
                Stop = True
            # Move the index to the parent to keep the properties
            i = i // 2

    def insert(self, k):
        """
        Inserts a value into the heap
        """
        # Append the element to the heap
        self.heap_list.append(k)
        # Increase the size of the heap.
        self.current_size += 1
        # Move the element to its position from bottom to the top
        self.sift_up(self.current_size)

    def sift_down(self, i):
        # if the current node has at least one child
        while (i * 2) <= self.current_size:
            # Get the index of the min child of the current node
            mc = self.min_child(i)
            # Swap the values of the current element is greater than its min child
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
                self.heap_list[i][3] = i
                self.heap_list[mc][3] = mc
            i = mc

    def min_child(self, i):
        # If the current node has only one child, return the index of the unique child
        if (i * 2) + 1 > self.current_size:
            return i * 2
        else:
            # Herein the current node has two children
            # Return the index of the min child according to their values
            if self.heap_list[i * 2] < self.heap_list[(i * 2) + 1]:
                return i * 2
            else:
                return (i * 2) + 1

    def delete_min(self):
        # Equal to 1 since the heap list was initialized with a value
        if len(self.heap_list) == 1:
            return 'Empty heap'

        # Get root of the heap (The min value of the heap)
        root = self.heap_list[1]

        # Move the last value of the heap to the root
        self.heap_list[1] = self.heap_list[self.current_size]

        # Pop the last value since a copy was set on the root
        *self.heap_list, _ = self.heap_list

        # Decrease the size of the heap
        self.current_size -= 1

        # Move down the root (value at index 1) to keep the heap property
        self.sift_down(1)

        # Return the min value of the heap
        return root

    def build_heap(self, ar):
        self.heap_list = [len(ar)] + ar
        self.current_size = len(ar)
        for i in range(len(self.heap_list) - 1, 0, -1):
            self.sift_down(i)

    def heapify(self, i):
        self.sift_up(i)
        self.sift_down(i)


"""
Driver program
"""


def get_final_velocities(m1, v1, m2, v2):
    v2prime = 2 * m1 / (m1 + m2) * v1 - (m1 - m2) / (m1 + m2) * v2
    v1prime = (m1 - m2) / (m1 + m2) * v1 + 2 * m2 / (m1 + m2) * v2

    return v1prime, v2prime


def get_time_till_collision(x1, v1, x2, v2):
    if x1 == x2 and v2 - v1 > 0:
        return float('inf')
    if v1 == v2:
        return float('inf')
    if -(x2 - x1) / (v2 - v1) < 0:
        return float('inf')
    return -(x2 - x1) / (v2 - v1)


def rounded(collisions):
    return [(round(i[0], 4), i[1], round(i[2], 4))
            for i in collisions]


def listCollisions(M, x, v, m, T):
    my_heap = MinHeap()
    collisions = []
    current_time = 0
    possible_collisions = []
    X = [[i, 0] for i in x]
    for i in range(len(M) - 1):
        t = get_time_till_collision(x[i], v[i], x[i + 1], v[i + 1])
        possible_collisions.append([t, i, x[i] + v[i] * t, i])
    my_heap.build_heap(possible_collisions)

    while len(collisions) < m and current_time < T:
        collision = my_heap.delete_min()  # pop

        t = collision[0]
        i = collision[1]
        x = collision[2]
        current_time = t
        if current_time > T:
            break

        collisions.append(collision.copy())

        X[i][0], X[i][1] = X[i][0] + v[i] * (current_time - X[i][1]), current_time
        X[i + 1][0], X[i + 1][1] = X[i + 1][0] + v[i + 1] * (current_time - X[i + 1][1]), current_time

        collision[0] = float('inf')
        v[i], v[i + 1] = get_final_velocities(M[i], v[i], M[i + 1],
                                              v[i + 1])
        collision[0] = float('inf')
        collision[2] = float('inf')
        
        my_heap.insert(collision)

        if i != 0:
            X[i - 1][0], X[i - 1][1] = X[i - 1][0] + v[i - 1] * (current_time - X[i - 1][1]), current_time
            temp1 = possible_collisions[i - 1]
            t = get_time_till_collision(X[i - 1][0], v[i - 1], X[i][0], v[i])
            temp1[0] = current_time + t
            temp1[2] = X[i - 1][0] + v[i - 1] * t
            my_heap.heapify(temp1[3])

        if i != len(possible_collisions) - 1:
            X[i + 2][0], X[i + 2][1] = X[i + 2][0] + v[i + 2] * (current_time - X[i + 2][1]), current_time
            temp2 = possible_collisions[i + 1]
            t = get_time_till_collision(X[i + 1][0], v[i + 1], X[i + 2][0], v[i + 2])
            temp2[0] = current_time + t
            temp2[2] = X[i + 1][0] + v[i + 1] * t
            my_heap.heapify(temp2[3])

    return rounded(collisions)


print(listCollisions([1.0, 5.0], [1.0, 2.0], [3.0, 5.0], 100, 100.0))
print(listCollisions([1.0, 1.0, 1.0, 1.0], [-2.0, -1.0, 1.0, 2.0], [0.0, -1.0, 1.0, 0.0], 5,
                     5.0))
print(listCollisions([10000.0, 1.0, 100.0], [0.0, 1.0, 2.0], [0.0, 0.0, -1.0], 6, 10.0))
print(listCollisions([10000.0, 1.0, 100.0], [0.0, 1.0, 2.0], [0.0, 0.0, -1.0], 100, 1.5))
print(listCollisions([1, 1, 1, 1, 1, 1],
                     [0, 1, 2, 3, 4, 5],
                     [1, 0, 1, 0, 1, 0],
                     8,
                     100))
