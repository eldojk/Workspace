# coding=utf-8
"""
amzn, msft

http://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-k-times/

profit[t][i] = max(
                    profit[t][i-1],
                    max(price[i] – price[j] + profit[t-1][j]   for all j in range [0, i-1])
                    )

"""
from sys import maxint


def max_price(prices, n, k):
    dp = [[0 for i in range(n + 1)] for j in range(k + 1)]

    # profit on 0th day = 0. Also 0 transactions is 0.
    # hence first row and column is 0s

    for i in range(1, k + 1):  # max i transactions
        for j in range(1, n):  # j days

            max_so_far = -maxint
            for m in range(j):
                max_so_far = max(
                    max_so_far,
                    prices[j] - prices[m] + dp[i - 1][m]
                )

            dp[i][j] = max(
                dp[i][j - 1],
                max_so_far
            )

    return dp[k][n - 1]


if __name__ == '__main__':
    print max_price([10, 22, 5, 75, 65, 80], 6, 2)

