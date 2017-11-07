"""
amzn

https://www.quora.com/In-how-many-possible-ways-can-I-get-the-sum-of-N-with-1-to-N-1-coins-without-using-the-same-coin-again

DP[N][K] = DP[N-K][K-1]+  # using kth coin,
            DP[N][K-1]    # not using it

            or

Given a number k , Find no. of ways to make this number using sum of numbers from 1 to k-1
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def get_num_ways_to_make_k_using_1_to_k(n, k):
    dp = [[0 for i in range(k + 1)] for j in range(n + 1)]

    for i in range(k + 1):
        dp[0][i] = 1

    for i in range(1, n + 1):
        for j in range(1, k + 1):

            dp[i][j] = dp[i][j - 1]  # not using j

            if j <= i:
                dp[i][j] += dp[i - j][j - 1]  # using j

    print_matrix(dp)
    return dp[n][k]


if __name__ == '__main__':
    print get_num_ways_to_make_k_using_1_to_k(6, 5)
