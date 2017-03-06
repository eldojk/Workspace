"""
http://www.geeksforgeeks.org/distance-nearest-cell-1-binary-matrix/

Input : M = 3, N = 4
        mat[][] = {
                    0, 0, 0, 1,
                    0, 0, 1, 1,
                    0, 1, 1, 0
                  }
Output : 3 2 1 0
         2 1 0 0
         1 0 0 1
"""
from Queue import Queue


def is_valid(m, n, i, j):
    return (0 <= i < m) and (0 <= j < n)


def get_neighbours(m, n, i, j):
    valid_candidates = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]
    valid_neighbours = [tup for tup in valid_candidates if is_valid(m, n, tup[0], tup[1])]

    return valid_neighbours


def get_indices_of_1(m, n, matrix, dist_matrix):
    indices = Queue()
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1:
                indices.put(((i, j), 0))
                dist_matrix[i][j] = 0

    return indices


def get_initial_matrix(m, n):
    return [[-1 for i in range(n)] for j in range(m)]


def is_visited(i, j, matrix):
    return matrix[i][j] != -1


def get_distances(m, n, matrix):
    dist_matrix = get_initial_matrix(m, n)
    q = get_indices_of_1(m, n, matrix, dist_matrix)

    while not q.empty():
        item = q.get()
        index = item[0]
        dist = item[1]

        for neighbour in get_neighbours(m, n, index[0], index[1]):
            i = neighbour[0]
            j = neighbour[1]
            neighbour_distance = dist + 1

            if not is_visited(i, j, dist_matrix):
                dist_matrix[i][j] = neighbour_distance
                q.put(((i, j), neighbour_distance))

    return dist_matrix


if __name__ == '__main__':
    m = [[0, 0, 0, 1],
         [0, 0, 1, 1],
         [0, 1, 1, 0]]

    print get_distances(3, 4, m)
