# coding=utf-8
"""
http://algorithms.tutorialhorizon.com/dynamic-programming-coin-change-problem/

Given coins of certain denominations and a total, how many ways these coins can be combined to get the total

Base Cases:
if amount=0 then just return empty set to make the change, so 1 way to make the change.
if no coins given, 0 ways to change the amount.

Rest of the cases:
For every coin we have an option to include it in solution or exclude it.
check if the coin value is less than or equal to the amount needed, if yes then we will find ways by including that coin
and excluding that coin.
Include the coin: reduce the amount by coin value and use the sub problem solution (amount-v[i]).
Exclude the coin: solution for the same amount without considering that coin.
If coin value is greater than the amount then we can’t consider that coin, so solution will be without considering that
coin.
"""


def num_ways(coins, total):
    solution = [[1] + [0 for i in range(total)] for j in range(len(coins) + 1)]

    for i in range(1, len(coins) + 1):
        for j in range(1, total + 1):
            coin_val = coins[i - 1]
            amt = j

            if coin_val <= amt:
                solution[i][j] = solution[i - 1][j] + solution[i][j - coin_val]
            else:
                solution[i][j] = solution[i - 1][j]

    return solution[len(coins)][total]
