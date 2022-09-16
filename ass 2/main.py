def get_final_velocities(m1, v1, m2, v2):
    v1prime = 2 * m1 / (m1 + m2) * v1 - (m1 - m2) / (m1 + m2) * v2
    v2prime = (m1 - m2) / (m1 + m2) * v1 + 2 * m2 / (m1 + m2) * v2

    return v1prime, v2prime


def get_time_till_collision(x1, v1, x2, v2):
    if x1 == x2:
        return 0
    if v1 == v2:
        return float('inf')
    if -(x2 - x1) / (v2 - v1) < 0:
        return float('inf')
    return -(x2 - x1) / (v2 - v1)
