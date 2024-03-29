class MinHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def heap_up(self, i):
        Stop = False
        while (i // 2 > 0) and Stop == False:
            if self.heap_list[i] < self.heap_list[i // 2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
                self.heap_list[i][3] = i
                self.heap_list[i // 2][3] = i // 2
                Stop = True
            i = i // 2

    def insert(self, k):
        self.heap_list.append(k)
        self.current_size += 1
        self.heap_up(self.current_size)

    def heap_down(self, i):
        while (i * 2) <= self.current_size:
            mc = self.min_child(i)
            if self.heap_list[i] > self.heap_list[mc]:
                self.heap_list[i], self.heap_list[mc] = self.heap_list[mc], self.heap_list[i]
                self.heap_list[i][3] = i
                self.heap_list[mc][3] = mc
            i = mc

    def min_child(self, i):
        if (i * 2) + 1 > self.current_size:
            return i * 2
        else:
            if self.heap_list[i * 2] < self.heap_list[(i * 2) + 1]:
                return i * 2
            else:
                return (i * 2) + 1

    def pop(self):
        if len(self.heap_list) == 1:
            return

        root = self.heap_list[1]

        self.heap_list[1] = self.heap_list[self.current_size]

        *self.heap_list, _ = self.heap_list

        self.current_size -= 1

        self.heap_down(1)

        return root

    def build_heap(self, ar):
        self.heap_list = [len(ar)] + ar
        self.current_size = len(ar)
        for i in range(len(self.heap_list) - 1, 0, -1):
            self.heap_down(i)

    def heapify(self, i):
        self.heap_up(i)
        self.heap_down(i)


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
        collision = my_heap.pop()  # pop

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
