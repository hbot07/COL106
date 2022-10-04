import heapq

def _siftdown(heap, startpos, pos):
    newitem = heap[pos]
    # Follow the path to the root, moving parents down until finding a place
    # newitem fits.
    while pos > startpos:
        parentpos = (pos - 1) >> 1
        parent = heap[parentpos]
        if newitem < parent:
            heap[pos] = parent
            pos = parentpos
            continue
        break
    heap[pos] = newitem


def _siftup(heap, pos):
    endpos = len(heap)
    startpos = pos
    newitem = heap[pos]
    # Bubble up the smaller child until hitting a leaf.
    childpos = 2*pos + 1    # leftmost child position
    while childpos < endpos:
        # Set childpos to index of smaller child.
        rightpos = childpos + 1
        if rightpos < endpos and not heap[childpos] < heap[rightpos]:
            childpos = rightpos
        # Move the smaller child up.
        heap[pos] = heap[childpos]
        pos = childpos
        childpos = 2*pos + 1
    # The leaf at pos is empty now.  Put newitem there, and bubble it up
    # to its final resting place (by sifting its parents down).
    heap[pos] = newitem
    _siftdown(heap, startpos, pos)


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
    collisions = []
    current_time = 0
    possible_collisions = []
    X = [[i, 0] for i in x]
    for i in range(len(M) - 1):
        t = get_time_till_collision(x[i], v[i], x[i + 1], v[i + 1])
        possible_collisions.append([t, i, x[i] + v[i] * t])
    heap = possible_collisions.copy()
    heapq.heapify(heap)

    while len(collisions) < m and current_time < T:
        collision = heapq.heappop(heap)  # pop

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
        heapq.heappush(heap, collision)  # push

        if i != 0:
            X[i - 1][0], X[i - 1][1] = X[i - 1][0] + v[i - 1] * (current_time - X[i - 1][1]), current_time
            temp1 = possible_collisions[i - 1]
            t = get_time_till_collision(X[i - 1][0], v[i - 1], X[i][0], v[i])
            temp1[0] = current_time + t
            temp1[2] = X[i - 1][0] + v[i - 1] * t


        if i != len(possible_collisions) - 1:
            X[i + 2][0], X[i + 2][1] = X[i + 2][0] + v[i + 2] * (current_time - X[i + 2][1]), current_time
            temp2 = possible_collisions[i + 1]
            t = get_time_till_collision(X[i + 1][0], v[i + 1], X[i + 2][0], v[i + 2])
            temp2[0] = current_time + t
            temp2[2] = X[i + 1][0] + v[i + 1] * t


        heapq.heapify(heap)  # heapify

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
