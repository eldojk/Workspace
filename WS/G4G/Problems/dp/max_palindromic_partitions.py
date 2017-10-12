"""
amzn

http://www.geeksforgeeks.org/given-a-string-print-all-possible-palindromic-partition/
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def is_pal(string, i, j):
    while i < j:
        if string[i] != string[j]:
            return False

        i += 1
        j -= 1

    return True


def max_pal(string):
    n = len(string)
    dp = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        dp[i][i] = 1

        j = i + 1
        if j < n:
            dp[i][j] = 2 if string[i] == string[j] else 1

    for l in range(2, n):
        for i in range(n):

            j = i + l

            if j < n:
                dp[i][j] = max(
                    dp[i][j - 1],
                    dp[i + 1][j - 1]
                )

                if is_pal(string, i, j):
                    dp[i][j] += 1

    print_matrix(dp)
    return dp[0][n - 1]


if __name__ == '__main__':
    print max_pal('NITIN')
    print ''
    print max_pal('geeks')
