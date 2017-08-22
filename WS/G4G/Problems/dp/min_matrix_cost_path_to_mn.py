"""
http://www.geeksforgeeks.org/dynamic-programming-set-6-min-cost-path/

	1	3	6
	5	9	5
	6	10	8
"""


def print_matrix(m):
    for row in m:
        print ' '.join(map(str, row))


def min_cost_path_to_mn(matrix, m, n):
    # copying matrix
    cost = [[j for j in matrix[i]] for i in range(m)]

    # summing over first row and column
    for j in range(1, n):
        cost[0][j] = cost[0][j - 1] + matrix[0][j]

    for i in range(1, m):
        cost[i][0] = cost[i - 1][0] + matrix[i][0]

    for i in range(1, m):
        for j in range(1, n):
            cost[i][j] = matrix[i][j] + min(
                cost[i - 1][j],
                cost[i - 1][j - 1],
                cost[i][j - 1]
            )

    return cost[m - 1][n - 1]


if __name__ == '__main__':
    m = [
        [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]
    ]

    print min_cost_path_to_mn(m, 3, 3)


def min_cost_path_to_mn_memo(matrix, i, j, m, n, dp):
    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = matrix[i][j] + min(
        min_cost_path_to_mn_memo(matrix, i - 1, j, m, n, dp),
        min_cost_path_to_mn_memo(matrix, i - 1, j - 1, m, n, dp),
        min_cost_path_to_mn_memo(matrix, i, j - 1, m, n, dp)
    )

    return dp[i][j]


def min_cost_path_to_mn_memoized(matrix, m, n):
    dp = [[-1 for i in matrix[0]] for j in matrix]

    dp[0][0] = matrix[0][0]

    for j in range(1, n):
        dp[0][j] = dp[0][j - 1] + matrix[0][j]

    for i in range(1, m):
        dp[i][0] = dp[i - 1][0] + matrix[i][0]

    return min_cost_path_to_mn_memo(matrix, m - 1, n - 1, m, n, dp)


if __name__ == '__main__':
    m = [
        [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3]
    ]

    print min_cost_path_to_mn_memoized(m, 3, 3)