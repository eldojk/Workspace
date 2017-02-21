"""
http://www.geeksforgeeks.org/find-number-of-islands/
"""


def is_valid(m, n, i, j):
    return (0 <= i < m) and (0 <= j < n)


def get_neighbours(matrix, m, n, i, j):
    valid_candidates = [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1), (i - 1, j - 1), (i + 1, j - 1), (i - 1, j + 1),
                        (i + 1, j + 1)]
    valid_neighbours = [tup for tup in valid_candidates if is_valid(m, n, tup[0], tup[1])]

    actual_neighbours = []
    for n in valid_neighbours:
        if matrix[n[0]][n[1]] == 1:
            actual_neighbours.append(n)

    return actual_neighbours


VISITED = None


def dfs(matrix, m, n, i, j):
    global VISITED
    VISITED[i][j] = True
    for neighbour in get_neighbours(matrix, m, n, i, j):
        _i = neighbour[0]
        _j = neighbour[1]

        if not VISITED[_i][_j]:
            dfs(matrix, m, n, _i, _j)


def get_num_islands(matrix):
    global VISITED
    m = len(matrix)
    n = len(matrix[0])
    VISITED = [[False for i in range(n)] for j in range(m)]
    connected_components = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 1 and not VISITED[i][j]:
                dfs(matrix, m, n, i, j)
                connected_components += 1

    return connected_components


if __name__ == '__main__':
    island_data_set = [[1, 1, 0, 0, 0],
                       [0, 1, 0, 0, 1],
                       [1, 0, 0, 1, 1],
                       [0, 0, 0, 0, 0],
                       [1, 0, 1, 0, 1]]

    print get_num_islands(island_data_set)
