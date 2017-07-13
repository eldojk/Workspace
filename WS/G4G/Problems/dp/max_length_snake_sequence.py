# coding=utf-8
"""
http://www.geeksforgeeks.org/find-maximum-length-snake-sequence/

A snake sequence is made up of adjacent numbers in the grid such that for each number,
the number on the right or the number below it is +1 or -1 its value.
For example, if you are at location (x, y) in the grid, you can either move right
i.e. (x, y+1) if that number is ± 1 or move down i.e. (x+1, y) if that number is ± 1.

For example,

9, 6, 5, 2
8, 7, 6, 5
7, 3, 1, 6
1, 1, 1, 7

In above grid, the longest snake sequence is: (9, 8, 7, 6, 5, 6, 7)

T[0][0] = 1
T[i][j] = max(T[i][j], T[i][j – 1] + 1) if M[i][j] = M[i][j – 1] ± 1
T[i][j] = max(T[i][j], T[i – 1][j] + 1) if M[i][j] = M[i – 1][j] ± 1
"""


def max_seq(matrix):
    dp = [[1 for i in matrix[0]] for j in matrix]

    max_len = 0

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            if i == 0 and j == 0:
                continue

            if i > 0 and abs(matrix[i - 1][j] - matrix[i][j]) == 1:
                dp[i][j] = max(
                    dp[i][j],
                    dp[i - 1][j] + 1
                )

                if dp[i][j] > max_len:
                    max_len = dp[i][j]

            if j > 0  and abs(matrix[i][j - 1] - matrix[i][j]) == 1:
                dp[i][j] = max(
                    dp[i][j],
                    dp[i][j - 1] + 1
                )

                if dp[i][j] > max_len:
                    max_len = dp[i][j]

    return max_len


if __name__ == '__main__':
    m = [
        [9, 6, 5, 2],
        [8, 7, 6, 5],
        [7, 3, 1, 6],
        [1, 1, 1, 7]
    ]

    print max_seq(m)