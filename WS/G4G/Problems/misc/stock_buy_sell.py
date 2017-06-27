"""
amzn msft

http://www.geeksforgeeks.org/stock-buy-sell/

The cost of a stock on each day is given in an array, find the max profit that you can make
by buying and selling in those days. For example, if the given array is
{100, 180, 260, 310, 40, 535, 695}, the maximum profit can earned by buying on day 0,
selling on day 3. Again buy on day 4 and sell on day 6. If the given array of prices
is sorted in decreasing order, then profit cannot be earned at all.

1. Find the local minima and store it as starting index. If not exists, return.
2. Find the local maxima. and store it as ending index. If we reach the end, set the end as ending index.
3. Update the solution (Increment count of buy sell pairs)
4. Repeat the above steps if end is not reached.
"""


def find_local_minima(array, i, n):
    while i < n - 1 and array[i] >= array[i + 1]:
        i += 1

    return i


def find_local_maxima(array, i, n):
    while i < n - 1 and array[i + 1] >= array[i]:
        i += 1

    return i


def maximize_profit(array):
    n = len(array)
    buys = []
    i = 0

    while i < n:
        i = find_local_minima(array, i, n)

        if i == n - 1:
            break

        tup = [None, None]
        tup[0] = i
        i += 1

        i = find_local_maxima(array, i, n)

        tup[1] = i

        buys.append(tup)

    if len(buys) == 0:
        print 'No way to make profit'

    else:
        print buys


if __name__ == '__main__':
    a = [100, 180, 260, 310, 40, 535, 695]
    maximize_profit(a)
