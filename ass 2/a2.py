def get_final_velocities(m1, v1, m2, v2):
    v2prime = 2 * m1 / (m1 + m2) * v1 - (m1 - m2) / (m1 + m2) * v2
    v1prime = (m1 - m2) / (m1 + m2) * v1 + 2 * m2 / (m1 + m2) * v2

    return v1prime, v2prime


def get_time_till_collision(x1, v1, x2, v2):
    if x1 == x2:  # smth weird
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
    colin = []
    time_till_collision_list = [None for i in range(len(M)-1)]
    while m > len(collisions):
        for i in colin:
            time_till_collision_list[i] = float('inf')
        for i in range(len(M) - 1):
            time_till_collision_list[i] = (get_time_till_collision(x[i], v[i], x[i + 1], v[i + 1]))
        colin = []

        min_index = 0
        for i in range(len(time_till_collision_list)):
            if time_till_collision_list[min_index] > time_till_collision_list[i]:
                min_index = i

        for i in range(len(time_till_collision_list)):
            if time_till_collision_list[min_index] == time_till_collision_list[i]:
                colin.append(i)

        current_time += time_till_collision_list[min_index]
        if current_time > T:
            break
        for i in range(len(x)):
            x[i] += v[i] * time_till_collision_list[min_index]

        v[min_index], v[min_index + 1] = get_final_velocities(M[min_index], v[min_index], M[min_index + 1],
                                                              v[min_index + 1])

        for i in colin:
            collisions.append((current_time, i, x[i]))

    return rounded(collisions)


print(listCollisions([1.0, 5.0], [1.0, 2.0], [3.0, 5.0], 100, 100.0))
print(listCollisions([1.0, 1.0, 1.0, 1.0], [-2.0, -1.0, 1.0, 2.0], [0.0, -1.0, 1.0, 0.0], 5,
                     5.0))
print(listCollisions([10000.0, 1.0, 100.0], [0.0, 1.0, 2.0], [0.0, 0.0, -1.0], 6, 10.0))
print(listCollisions([10000.0, 1.0, 100.0], [0.0, 1.0, 2.0], [0.0, 0.0, -1.0], 100, 1.5))
