"""
amzn msft

http://www.geeksforgeeks.org/print-a-given-matrix-in-spiral-form/
(this is not zig zag printing)
"""


def _print_sprl(matrix, i, j, m, n):
    for k in range(j, n + 1):
        print matrix[i][k],

    for k in range(i + 1, m + 1):
        print matrix[k][n],

    if i < m:
        for k in reversed(range(j, n)):
            print matrix[m][k],

    if j < n:
        for k in reversed(range(i + 1, m)):
            print matrix[k][j],


def print_spiral_matrix_repr(matrix):
    i = 0
    m = len(matrix) - 1
    j = 0
    n = len(matrix[0]) - 1

    while i <= m and j <= n:
        _print_sprl(matrix, i, j, m, n)

        i += 1
        m -= 1
        j += 1
        n -= 1


if __name__ == '__main__':
    m = [
        [1,  2,  3,  4,  5,  6],
        [7,  8,  9,  10, 11, 12],
        [13, 14, 15, 16, 17, 18]
    ]
    print_spiral_matrix_repr(m)

    print ''

    m = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12],
        [13, 14, 15, 16]
    ]
    print_spiral_matrix_repr(m)

    print ''

    m = [
        [1, 2, 3, 4, 5],
        [6, 7, 8, 9, 10],
        [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20],
        [21, 22, 23, 24, 25]
    ]
    print_spiral_matrix_repr(m)
