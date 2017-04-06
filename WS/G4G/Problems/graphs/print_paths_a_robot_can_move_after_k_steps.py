# coding=utf-8
"""
Given a 2-D grid, number of steps to take, say k and intial position of a Robot. print the paths possible from initial
position after k steps. Robot can move in top, right, left, bottom. In one path, robot can’t move to the location it has
previously visited.
"""


def is_valid(grid, tup):
    i = tup[0]
    j = tup[1]
    max_i = len(grid)
    max_j = len(grid[0])

    return 0 <= i < max_i and 0 <= j < max_j


def get_all_neighbors(grid, i, j):
    paths = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

    valid_paths = [p for p in paths if is_valid(grid, p)]
    return valid_paths


def print_paths(grid, i, j, k, visited, paths):
    visited[i][j] = True
    paths.append(grid[i][j])

    if k == 0:
        print ' '.join(map(str, paths))
        visited[i][j] = False
        paths.pop()
        return

    for neighbour in get_all_neighbors(grid, i, j):
        m = neighbour[0]
        n = neighbour[1]

        if visited[m][n]:
            continue

        print_paths(grid, m, n, k - 1, visited, paths)

    paths.pop()
    visited[i][j] = False


if __name__ == '__main__':
    g = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 0, 1, 2],
        [3, 4, 5, 6]
    ]
    v = [[False for i in range(4)] for j in range(4)]
    print_paths(g, 2, 1, 2, v, [])
