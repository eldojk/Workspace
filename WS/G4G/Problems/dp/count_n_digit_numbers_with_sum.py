"""
http://www.geeksforgeeks.org/count-of-n-digit-numbers-whose-sum-of-digits-equals-to-given-sum/

The last digit can be k, that means, count n - 1 digit nums with sum -k sum for all k

	0	1	2	3	4	5
0	1	0	0	0	0	0
1	1	1
2	1
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def count_n_digit_nums_of_sum(n, s):
    dp = [[0 for i in range(s + 1)] for j in range(n + 1)]

    for i in range(s + 1):
        dp[0][i] = 0

    for i in range(n + 1):
        dp[i][0] = 1

    for num in range(1, n + 1):
        for _sum in range(1, s + 1):

            for last_digit in range(10):
                if last_digit > _sum:
                    break

                dp[num][_sum] += dp[num - 1][_sum - last_digit]

    print_matrix(dp)
    return dp[n][s]


if __name__ == '__main__':
    print count_n_digit_nums_of_sum(2, 5)
