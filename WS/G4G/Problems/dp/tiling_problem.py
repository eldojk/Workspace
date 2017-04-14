"""
http://www.geeksforgeeks.org/count-number-of-ways-to-fill-a-n-x-4-grid-using-1-x-4-tiles/

if we place tile vertically, then remaining can be defined as dp(n - 1),
If we place it horizontally, then the remaining three cells on top of the tile also
have to be horizontal => dp(n - 4)

dp(n) = dp(n - 1) + dp(n - 4)
"""


def ways_to_tile(n):
    dp = [0 for i in range(n + 1)]

    dp[1] = 1
    dp[2] = 1
    dp[3] = 1
    dp[4] = 2

    for i in range(5, n + 1):
        dp[i] = dp[i - 1] + dp[i - 4]

    return dp[n]


if __name__ == '__main__':
    print ways_to_tile(5)