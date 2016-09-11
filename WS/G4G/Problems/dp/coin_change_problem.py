"""
https://www.youtube.com/watch?&v=NJuKJ8sasGk TUSHAR ROY explains

sys.maxint
"""
from sys import maxint


def find_min_coins(coins, value):
    value_arr = [0] + [maxint for i in range(value)]
    last_used = [-1 for i in range(value + 1)]

    for coin in coins:
        for i in range(value + 1):
            if i >= coin:
                value_arr[i] = min(value_arr[i], 1 + value_arr[i - coin])
                last_used[i] = coin

    return value_arr[value]
