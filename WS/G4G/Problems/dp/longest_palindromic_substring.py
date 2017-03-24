"""
http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

        b	a	b	a	c	s
        0	1	2	3	4	5
-----------------------------
b	0	1	1	3	3	3	3
a	1		1	1	3	3	3
b	2			1	1	1	1
a	3				1	1	1
c	4					1	1
s	5						1


l[i,j] = length of longest palindromic substring from i to j

if i = j :
    1
if i - j == 1:
    2 if a[i] == b[j]
    1 else
else:
    2 + l[i+1, j-1] if a[i] == a[j]
    max (l[i, j-1], l[i+1,j])  # try string removing first character and last character
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def longest_palindromic_substring(string):
    dp = [[0 for i in string] for j in string]

    # adding base cases
    for i in range(len(string)):
        dp[i][i] = 1

        j = i + 1
        if j < len(string):
            dp[i][j] = 1 if string[i] != string[j] else 2

    max_index = len(string) - 1
    for l in range(2, len(string)):
        for i in range(len(string)):

            j = i + l

            if j <= max_index:
                if string[i] == string[j]:
                    dp[i][j] = 2 + dp[i + 1][j - 1]
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])

    # print_matrix(dp)
    return dp[0][max_index]


if __name__ == '__main__':
    print longest_palindromic_substring('babacs')
