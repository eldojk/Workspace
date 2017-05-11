"""
amzn

http://www.programcreek.com/2014/05/leetcode-longest-increasing-path-in-a-matrix-java/
"""


DX = [-1, 1, 0, 0]
DY = [0, 0, -1, 1]


def dfs(matrix, i, j, dp, m, n):
    if dp[i][j] != 0:
        return dp[i][j]

    for k in range(4):
        x = i + DX[k]
        y = j + DY[k]

        if 0 <= x < m and 0 <= y < n and matrix[x][y] > matrix[i][j]:
            dp[i][j] = max(
                dp[i][j],
                1 + dfs(matrix, x, y, dp, m, n)
            )

    return dp[i][j]


def longest_increasing_path_len(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for i in range(n)] for j in range(m)]

    longest = 0

    for i in range(m):
        for j in range(n):
            longest = max(
                longest,
                dfs(matrix, i, j, dp, m, n)
            )

    return longest
