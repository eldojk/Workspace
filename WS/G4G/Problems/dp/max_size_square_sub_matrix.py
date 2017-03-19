"""
http://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/

sum_matrix[i][j] represents the size of matrix with i, j and the bottom right cell
"""
from copy import copy


def max_size_sub_matrix(matrix, m, n):
    sum_matrix = copy(matrix)

    for i in range(1, m):
        for j in range(1, n):

            # if you include one more cell the size of square matrix
            # can only be as high as 1 plus the smallest adjacent cell
            if matrix[i][j] == 1:
                sum_matrix[i][j] = min(
                    sum_matrix[i - 1][j],
                    sum_matrix[i][j - 1],
                    sum_matrix[i - 1][j - 1]
                ) + 1

            # can't include the cell if its 0
            else:
                sum_matrix[i][j] = 0

    return max([max(row) for row in sum_matrix])


if __name__ == '__main__':
    m = [
        [0, 1, 1, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 1, 1, 1, 0],
        [1, 1, 1, 1, 0],
        [1, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ]

    print max_size_sub_matrix(m, 6, 5)