"""
amzn

http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

dp[i][j] is true if string from i through j including j is palindrome

We start with length 1 string and progress upwards
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def longest_palindromic_substring(string):
    dp = [[False for i in string] for j in string]
    n = len(string)
    max_len = 1

    for i in range(n):
        dp[i][i] = True

        j = i + 1

        if j < n and string[i] == string[j]:
            dp[i][j] = True
            max_len = 2

    for l in range(2, n):
        for i in range(n):
            j = i + l

            if j < n:

                if string[i] == string[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    max_len = max(
                        max_len,
                        j - i + 1
                    )
    return max_len


if __name__ == '__main__':
    print longest_palindromic_substring('babacs')
