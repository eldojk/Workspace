# coding=utf-8
"""
amzn, msft

http://www.geeksforgeeks.org/wildcard-pattern-matching/

Given a text and a wildcard pattern, implement wildcard pattern matching algorithm that finds if wildcard pattern is
matched with text. The matching should cover the entire text (not partial text).

The wildcard pattern can include the characters ‘?’ and ‘*’
‘?’ – matches any single character
‘*’ – Matches any sequence of characters (including the empty sequence)

// both text and pattern are null
T[0][0] = true;

// pattern is null
T[i][0] = false;

// text is null
T[0][j] = T[0][j - 1] if pattern[j – 1] is '*'
"""


def match(text, pattern):
    n = len(text)
    m = len(pattern)

    # empty pattern can only match with empty string
    if m == 0:
        return n == 0

    dp = [[False for i in range(m + 1)] for j in range(n + 1)]

    dp[0][0] = True

    for j in range(1, m + 1):
        if pattern[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]

    for i in range(1, n + 1):
        for j in range(1, m + 1):

            # ignore the * (consider * for empty string)
            # or match ith character or more
            if pattern[j - 1] == '*':
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]

            elif pattern[j - 1] == '?' or text[i - 1] == pattern[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]

            else:
                dp[i][j] = False

    return dp[n][m]


if __name__ == '__main__':
    print match('baaabab', '*****ba*****ab')
