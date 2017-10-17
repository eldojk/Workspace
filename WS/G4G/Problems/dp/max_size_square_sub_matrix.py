"""
amzn

http://www.geeksforgeeks.org/maximum-size-sub-matrix-with-all-1s-in-a-binary-matrix/

size_matrix[i][j] represents the size of matrix with i, j and the bottom right cell
"""
from copy import copy


def max_size_sub_matrix(matrix, m, n):
    size_matrix = copy(matrix)
    max_size = 0

    for i in range(1, m):
        for j in range(1, n):

            # if you include one more cell the size of square matrix
            # can only be as high as 1 plus the smallest adjacent cell
            # if all three are 1 we get 1, if one is zero, it has to be
            # at most the size of minimum + 1
            if matrix[i][j] == 1:
                size_matrix[i][j] = min(
                    size_matrix[i - 1][j],
                    size_matrix[i][j - 1],
                    size_matrix[i - 1][j - 1]
                ) + 1

                max_size = max(size_matrix[i][j], max_size)
            # can't include the cell if its 0
            else:
                size_matrix[i][j] = 0

    return max_size


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