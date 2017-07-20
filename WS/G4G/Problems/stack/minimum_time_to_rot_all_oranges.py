"""
amzn

http://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/
"""
from Queue import Queue


DELIMITER = 'T'


def get_rotten_oranges(matrix, m, n):
    q = Queue()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 2:
                q.put((i, j))

    return q


def is_valid(i, j, m, n):
    return (0 <= i < m) and (0 <= j < n)


def rot_neighbouring_oranges(matrix, i, j, q, m, n):
    a = [1, -1, 0, 0]
    b = [0, 0, 1, -1]
    rotten_now = []

    for k in range(4):
        x = i + a[k]
        y = j + b[k]

        if is_valid(x, y, m, n) and matrix[x][y] == 1:
            rotten_now.append((x, y))
            q.put((x, y))

    for r in rotten_now:
        c = r[0]
        d = r[1]
        matrix[c][d] = 2


def is_all_rotten(matrix, m, n):
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                return False

    return True


def time_to_rot(matrix, m, n):
    t = -1
    q = get_rotten_oranges(matrix, m, n)
    q.put(DELIMITER)
    prev_is_delimiter = False

    while not q.empty():
        el = q.get()

        if el != DELIMITER:
            x = el[0]
            y = el[1]
            rot_neighbouring_oranges(matrix, x, y, q, m, n)

        else:
            t += 1

            if is_all_rotten(matrix, m, n):
                t += 1
                break

            elif prev_is_delimiter:
                print 'Nope'
                return None

            else:
                q.put(DELIMITER)

        prev_is_delimiter = (el == DELIMITER)

    return t


if __name__ == '__main__':
    t1 = [
        [2, 1, 0, 2, 1],
        [1, 0, 1, 2, 1],
        [1, 0, 0, 2, 1]
    ]

    t2 = [
        [2, 1, 0, 2, 1],
        [0, 0, 1, 2, 1],
        [1, 0, 0, 2, 1]
    ]

    print time_to_rot(t1, 3, 5)
    print '---------------------'
    print time_to_rot(t2, 3, 5)
