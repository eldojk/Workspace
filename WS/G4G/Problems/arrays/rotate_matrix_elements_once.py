"""
msft

http://www.geeksforgeeks.org/rotate-matrix-elements/

Input
1    2    3
4    5    6
7    8    9

Output:
4    1    2
7    5    3
8    9    6

For 4*4 matrix
Input:
1    2    3    4
5    6    7    8
9    10   11   12
13   14   15   16

Output:
5    1    2    3
9    10   6    4
13   11   7    8
14   15   16   12
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def rotate_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    i = 0
    j = 0

    while i < m and j < n:

        if i == m - 1 or j == n - 1:
            break

        prev = matrix[i + 1][j]

        for c in range(j, n):
            curr = matrix[i][c]
            matrix[i][c] = prev
            prev = curr

        i += 1

        for r in range(i, m):
            curr = matrix[r][n - 1]
            matrix[r][n - 1] = prev
            prev = curr

        n -= 1

        c = n - 1
        while c >= j:
            curr = matrix[m - 1][c]
            matrix[m - 1][c] = prev
            prev = curr
            c -= 1

        m -= 1

        r = m - 1
        while r >= i:
            curr = matrix[r][j]
            matrix[r][j] = prev
            prev = curr
            r -= 1

        j += 1

    print_matrix(matrix)


if __name__ == '__main__':
    rotate_matrix(
        [
            [1,  2,  3,  4],
            [5,  6,  7,  8],
            [9,  10, 11, 12],
            [13, 14, 15, 16]
        ]
    )

    print ''

    rotate_matrix(
        [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
    )