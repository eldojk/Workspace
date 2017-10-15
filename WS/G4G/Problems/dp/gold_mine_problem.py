"""
amzn

http://www.geeksforgeeks.org/gold-mine-problem/

Input : mat[][] = {{1, 3, 3},
                   {2, 1, 4},
                  {0, 6, 4}};
Output : 12
{(1,0)->(2,1)->(2,2)}

Input: mat[][] = { {1, 3, 1, 5},
                   {2, 2, 4, 1},
                   {5, 0, 2, 3},
                   {0, 6, 1, 2}};
Output : 16
(2,0) -> (1,1) -> (1,2) -> (0,3) OR
(2,0) -> (3,1) -> (2,2) -> (2,3)

Input : mat[][] = {{10, 33, 13, 15},
                  {22, 21, 04, 1},
                  {5, 0, 2, 3},
                  {0, 6, 14, 2}};
Output : 83
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def is_valid(i, j, m, n):
    return 0 <= i < m and 0 <= j < n


def max_gold(matrix):
    m = len(matrix)
    n = len(matrix[0])
    dp = [[0 for i in range(n)] for j in range(m)]

    for i in range(m):
        dp[i][0] = matrix[i][0]

    for j in range(1, n):
        for i in range(m):

            possible_previous_positions = [(i - 1, j - 1), (i + 1, j - 1), (i, j - 1)]

            for c in possible_previous_positions:
                x = c[0]
                y = c[1]

                if is_valid(x, y, m, n):
                    dp[i][j] = max(
                        dp[i][j],
                        matrix[i][j] + dp[x][y]
                    )

    max_gold_collected = 0
    for i in range(m):
        max_gold_collected = max(
            max_gold_collected,
            dp[i][n - 1]
        )

    # print_matrix(dp)
    return max_gold_collected


if __name__ == '__main__':
    m = [
        [1, 3, 1, 5],
        [2, 2, 4, 1],
        [5, 0, 2, 3],
        [0, 6, 1, 2]
    ]

    print max_gold(m)
