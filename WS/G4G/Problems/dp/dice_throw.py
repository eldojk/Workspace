"""
http://www.geeksforgeeks.org/dice-throw-problem/

Let the function to find X from n dice is: Sum(m, n, X)
The function can be represented as:
Sum(m, n, X) = Finding Sum (X - 1) from (n - 1) dice plus 1 from nth dice
               + Finding Sum (X - 2) from (n - 1) dice plus 2 from nth dice
               + Finding Sum (X - 3) from (n - 1) dice plus 3 from nth dice
                  ...................................................
                  ...................................................
                  ...................................................
              + Finding Sum (X - m) from (n - 1) dice plus m from nth dice

So we can recursively write Sum(m, n, x) as following
Sum(m, n, X) = Sum(m, n - 1, X - 1) +
               Sum(m, n - 1, X - 2) +
               .................... +
               Sum(m, n - 1, X - m)

dp(x,n) = sum(dp(x-vi, n - 1) for vi in values such that x - vi >=0)
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def num_ways(m, n, x):
    dp = [[0 for i in range(x + 1)] for j in range(n + 1)]

    for i in range(1, x + 1):
        dp[1][i] = 1

    for i in range(2, n + 1):
        for j in range(1, x + 1):

            for k in range(1, m + 1):
                if j >= k:
                    dp[i][j] += dp[i - 1][j - k]

    return dp[n][x]


if __name__ == '__main__':
    print num_ways(4, 2, 1)
    print num_ways(2, 2, 3)
    print num_ways(6, 3, 8)
    print num_ways(4, 2, 5)
    print num_ways(4, 3, 5)