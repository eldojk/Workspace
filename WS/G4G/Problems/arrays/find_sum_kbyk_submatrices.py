"""
amzn

http://www.geeksforgeeks.org/given-n-x-n-square-matrix-find-sum-sub-squares-size-k-x-k/
http://www.geeksforgeeks.org/print-maximum-sum-square-sub-matrix-of-given-size/
"""
from sys import maxint


def print_sums(matrix, k):
    n = len(matrix)
    r = n - k + 1

    k_stripe_sum_matrix = [[0 for i in range(n)] for j in range(r)]

    for j in range(n):
        for i in range(k):
            k_stripe_sum_matrix[0][j] += matrix[i][j]

    for j in range(n):
        for i in range(1, r):
            k_stripe_sum_matrix[i][j] = k_stripe_sum_matrix[i - 1][j] + matrix[k - 1 + i][j] - matrix[i - 1][j]

    # print
    max_sub_matrix_sum = -maxint
    mi = 0
    mj = 0

    for i in range(r):
        curr_sum = 0

        for j in range(k - 1, n):
            if j == k - 1:
                for m in range(k - 1):
                    curr_sum += k_stripe_sum_matrix[i][m]

            curr_sum += k_stripe_sum_matrix[i][j]

            if j - k + 1 > 0:
                curr_sum -= k_stripe_sum_matrix[i][j - k]

            print curr_sum, ' ',

            if curr_sum > max_sub_matrix_sum:
                max_sub_matrix_sum = curr_sum
                mi = i
                mj = j - k + 1

        print ''

    print ''
    print 'max sum sub matrix'
    for i in range(k):
        _i = mi + i
        for j in range(k):
            _j = mj + j
            print matrix[_i][_j], ' ',

        print ''


if __name__ == '__main__':
    m = [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 3, 3, 3, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5]
    ]
    print_sums(m, 3)

    print ''
    print ''

    m2 = [
        [1, 1, 1, 1, 1],
        [2, 2, 2, 2, 2],
        [3, 8, 6, 7, 3],
        [4, 4, 4, 4, 4],
        [5, 5, 5, 5, 5]
    ]

    print_sums(m2, 3)
