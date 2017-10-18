# coding=utf-8
"""
amzn, msft

http://www.geeksforgeeks.org/maximum-profit-by-buying-and-selling-a-share-at-most-k-times/

Let profit[t][i] represent maximum profit using at most t transactions up to day i (including day i).
Then the relation is:

profit[t][i] will be maximum of –

profit[t][i-1] which represents not doing any transaction on the ith day.

Maximum profit gained by selling on ith day. In order to sell shares on ith day,
we need to purchase it on any one of [0, i – 1] days. If we buy shares on jth day
and sell it on ith day, max profit will be price[i] – price[j] + profit[t-1][j]
where j varies from 0 to i-1. Here profit[t-1][j] is best we could have done
with one less transaction till jth day.

profit[t][i] = max(
                    profit[t][i-1],  # not selling on ith day
                    max(price[i] – price[j] + profit[t-1][j]   for all j in range [0, i-1])  # selling on ith day
                    )

"""
from sys import maxint

from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def max_price(prices, n, k):
    dp = [[0 for i in range(n)] for j in range(k + 1)]

    # profit on 0th day = 0. Also 0 transactions is 0.
    # hence first row and column is 0s

    for i in range(1, k + 1):  # max i transactions
        for j in range(1, n):  # I am selling on jth day

            max_so_far = -maxint
            for m in range(j):
                max_so_far = max(
                    max_so_far,
                    prices[j] - prices[m] + dp[i - 1][m]
                )

            dp[i][j] = max(
                dp[i][j - 1],  # not doing anything on jth day
                max_so_far  # max by doing on jth day
            )

    print_matrix(dp)
    return dp[k][n - 1]


if __name__ == '__main__':
    print max_price([10, 22, 5, 75, 65, 80], 6, 2)
