"""
amzn

http://www.geeksforgeeks.org/number-of-paths-with-exactly-k-coins/

Example:

Input:  k = 12
        mat[][] = { {1, 2, 3},
                    {4, 6, 5},
                    {3, 2, 1}
                  };
Output:  2
There are two paths with 12 coins
1 -> 2 -> 6 -> 2 -> 1
1 -> 2 -> 3 -> 5 -> 1


pathCount(m, n, k):   Number of paths to reach mat[m][n] from mat[0][0]
                      with exactly k coins

If (m == 0 and n == 0)
   return 1 if mat[0][0] == k else return 0
Else:
    pathCount(m, n, k) = pathCount(m-1, n, k - mat[m][n]) +
                         pathCount(m, n-1, k - mat[m][n])
"""


def path_count(matrix, dp, m, n, k):
    if m < 0 or n < 0:
        return 0

    if m == 0 and n == 0:
        return 1 if k == matrix[m][n] else 0

    if dp[m][n][k] != -1:
        return dp[m][n][k]

    dp[m][n][k] = path_count(matrix, dp, m - 1, n, k - matrix[m][n]) + \
                  path_count(matrix, dp, m, n - 1, k - matrix[m][n])

    return dp[m][n][k]


def find_paths_num(matrix, k):
    m = len(matrix) - 1
    n = len(matrix[0]) - 1

    dp = [[[-1 for x in range(k + 1)] for i in range(n + 1)] for j in range(m + 1)]
    return path_count(matrix, dp, m, n, k)


if __name__ == '__main__':
    mt = [
        [1, 2, 3],
        [4, 6, 5],
        [3, 2, 1]
    ]
    print find_paths_num(mt, 12)
