"""
#tricky
http://www.geeksforgeeks.org/a-matrix-probability-question/
"""


def is_in_matrix(x, y, m, n):
    return 0 <= x < m and 0 <= y < n


def probability(num, m, n, x, y):
    if not is_in_matrix(x, y, m, n):
        return 0.0

    if num == 0:
        return 1.0

    prob = 0.0

    prob += 0.25 * probability(num - 1, m, n, x - 1, y)

    prob += 0.25 * probability(num - 1, m, n, x + 1, y)

    prob += 0.25 * probability(num - 1, m, n, x, y - 1)

    prob += 0.25 * probability(num - 1, m, n, x, y + 1)

    return prob


if __name__ == '__main__':
    print probability(2, 5, 5, 1, 1)
