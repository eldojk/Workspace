"""
http://www.geeksforgeeks.org/longest-palindrome-substring-set-1/

	g	e	k	s	k	g
g	1	0	0	0	0	0
e		1	0	0	0	0
k			1	0	1	0
s				1	0	0
k					1	0
g						1
"""


def longest_palindromic_substring(string):
    matrix = [[False for i in range(len(string))] for j in range(len(string))]

    max_len = 1
    for i in range(len(string)):
        matrix[i][i] = True

    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            matrix[i][i + 1] = True
            max_len = 2

    max_index = len(string) - 1
    for l in range(2, len(string)):
        for i in range(len(string)):
            j = i + l

            if j <= max_index:
                matrix[i][j] = (string[i] == string[j]) and matrix[i + 1][j - 1]

                if matrix[i][j]:
                    length = j - i + 1
                    if length > max_len:
                        max_len = length

    return max_len

# print longest_palindromic_substring('gekskg')
