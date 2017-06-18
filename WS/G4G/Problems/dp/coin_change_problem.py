# coding=utf-8
"""
amzn

https://www.youtube.com/watch?&v=NJuKJ8sasGk TUSHAR ROY explains

    0   1   2   3   4   5   6   7   8   9   10  11  12  13
7   0   x   x   x   x   x   x   1   x   x   x   x   x   x
2   0   x   1   x   2   x   3   1   4   2   5   3   6   4
3   0   x   2   1   2   2   ....
6

^ using array is better

each coin we can use or not use,
if we use it, min[i] = 1 + min[i - val[i]]
or not use, min[i] = min[i]
"""
from sys import maxint

from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def find_min_coins(coins, value):
    value_arr = [0] + [maxint for i in range(value)]
    last_used = [-1 for i in range(value + 1)]

    for coin in coins:
        for i in range(value + 1):
            if i >= coin:
                value_arr[i] = min(value_arr[i], 1 + value_arr[i - coin])
                last_used[i] = coin

    return value_arr[value]


if __name__ == '__main__':

    print find_min_coins([7, 2, 3, 6], 13)


"""
amzn

http://www.geeksforgeeks.org/dynamic-programming-set-7-coin-change/

Given a value N, if we want to make change for N cents, and we have infinite supply of each of S = { S1, S2, .. , Sm}
valued coins, how many ways can we make the change? The order of coins doesn’t matter.

For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}. So output should be 4.
For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}.
So the output should be 5.

            Amount
last coin	0	1	2	3	4
0           1   0   0   0   0
1	        1	1	1	1	1
2	        1	1	2	2	3
3	        1	1	2	3	4
"""


def number_of_ways_to_make_change(n, coins):
    coins = [0] + coins
    num_ways = [[0 for i in range(n + 1)] for c in coins]

    for i in range(len(coins)):
        num_ways[i][0] = 1

    for i in range(1, len(coins)):

        for j in range(1, n + 1):

            last_coin = coins[i]
            val = j

            # this case we can't use ith coin
            if last_coin > val:
                num_ways[i][val] = num_ways[i - 1][val]
                continue

            # not using ith coin to make val or
            # using ith coin and making remaining value using coins till i
            num_ways[i][val] = \
                num_ways[i - 1][val] + num_ways[i][val - last_coin]

    return num_ways[len(coins) - 1][n]


if __name__ == '__main__':
    print ''
    print number_of_ways_to_make_change(4, [1, 2, 3])
    print number_of_ways_to_make_change(10, [2, 5, 3, 6])
