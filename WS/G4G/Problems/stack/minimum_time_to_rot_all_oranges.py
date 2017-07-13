"""
http://www.geeksforgeeks.org/minimum-time-required-so-that-all-oranges-become-rotten/
"""
from Queue import Queue


def is_valid_index(m, n, i, j):
    return (i < m and j < n) and (i >= 0 and j>=0)


def get_rotten_indices(array, m, n):
    indices = []
    for i in range(m):
        for j in range(n):
            if array[i][j] == 2:
                indices.append((i, j))

    return indices


def is_all_rotten(array, m, n):
    for i in range(m):
        for j in range(n):
            if array[i][j] == 1:
                return False

    return True


def rot_oranges(array, m, n):
    for i in range(m):
        for j in range(n):
            if array[i][j] == 2:
                if is_valid_index(m, n, i-1,j) and array[i-1][j] == 1:
                    array[i-1][j] = 2
                if is_valid_index(m, n, i+1, j) and array[i+1][j] == 1:
                    array[i+1][j] = 2
                if is_valid_index(m, n, i, j+1) and array[i][j+1] == 1:
                    array[i][j+1] = 2
                if is_valid_index(m, n, i, j-1) and array[i][j-1] == 1:
                    array[i][j-1] = 2


def time_to_rot(array, m, n):
    q = Queue()
    time = 0
    delim = 'T'
    considered = {}

    indices = get_rotten_indices(array, m, n)
    for index in indices:
        considered[index] = True
        q.put(index)

    q.put(delim)

    while not q.empty():
        element = q.get()

        if element == delim:
            time += 1
            rot_oranges(array, m, n)
            indices = get_rotten_indices(array, m, n)

            new_element_added = False

            for index in indices:
                if considered.get(index) is None:
                    q.put(index)
                    considered[index] = True
                    new_element_added = True

            if new_element_added:
                q.put(delim)

    return time if is_all_rotten(array, m, n) else None


t1 = [[2, 1, 0, 2, 1], [1, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
t2 = [[2, 1, 0, 2, 1], [0, 0, 1, 2, 1], [1, 0, 0, 2, 1]]
print time_to_rot(t1, 3, 5)
print time_to_rot(t2, 3, 5)
