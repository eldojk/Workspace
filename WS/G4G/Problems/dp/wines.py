"""
amzn

http://www.quora.com/Are-there-any-good-resources-or-tutorials-for-dynamic-programming-besides-the-TopCoder-tutorial/answer/Michal-Danil%C3%A1k?srid=3OBi&share=1
"""


def optimal_wine_sell_profit(wines, dp, begin, end):
    if begin > end:
        return 0

    if dp[begin][end] != -1:
        return dp[begin][end]

    n = len(wines)
    year = n - (end - begin + 1) + 1

    dp[begin][end] = max(
        (wines[begin] * year) + optimal_wine_sell_profit(wines, dp, begin + 1, end),  # sell from start
        (wines[end] * year) + optimal_wine_sell_profit(wines, dp, begin, end - 1)  # sell from end
    )

    return dp[begin][end]


def max_profit(wines):
    dp = [[-1 for i in range(len(wines))] for j in range(len(wines))]

    return optimal_wine_sell_profit(wines, dp, 0, len(wines) - 1)


if __name__ == '__main__':
    print max_profit([1, 3, 2, 4])