"""
amzn, msft

http://www.geeksforgeeks.org/inplace-rotate-square-matrix-by-90-degrees/
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def rotate(matrix):
    n = len(matrix)

    x = 0
    while x < n // 2:

        y = x

        while y < n - x - 1:
            temp = matrix[x][y]

            matrix[x][y] = matrix[n - y - 1][x]

            matrix[n - y - 1][x] = matrix[n - x - 1][n - y - 1]

            matrix[n - x - 1][n - y - 1] = matrix[y][n - x - 1]

            matrix[y][n - x - 1] = temp

            y += 1

        x += 1

    return matrix


if __name__ == '__main__':
    m = [
        ['a', 'b', 'c', 'd'],
        ['e', 'f', 'g', 'h'],
        ['i', 'j', 'k', 'l'],
        ['m', 'n', 'o', 'p']
    ]

    print_matrix(m)

    print ''

    print_matrix(rotate(m))

    print ''
    
    m = [
        ['a', 'b', 'c', 'd', 'q'],
        ['e', 'f', 'g', 'h', 'r'],
        ['i', 'j', 'k', 'l', 's'],
        ['m', 'n', 'o', 'p', 't'],
        ['u', 'v', 'x', 'y', 'z']
    ]

    print_matrix(m)

    print ''

    print_matrix(rotate(m))