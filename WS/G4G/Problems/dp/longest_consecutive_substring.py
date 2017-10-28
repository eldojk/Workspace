"""
msft

https://stackoverflow.com/questions/25301474/how-to-extract-longest-sub-string-having-distinct-consecutive-character-from-a
"""


def is_adjacent(a, b):
    return ord(a) - ord(b) == -1


def longest_consecutive_substring(string):
    l_index = 0
    l_len = 1

    dp = [1 for i in string]

    for i in range(1, len(string)):
        # considering i being the ending char of the longest consecutive substring
        # then length of it == 1 + length of the longest consecutive substring ending
        # at i - 1
        if is_adjacent(string[i - 1], string[i]):
            dp[i] = dp[i - 1] + 1

        if dp[i] > l_len:
            l_len = dp[i]
            l_index = i

    end = l_index
    start = end - l_len + 1
    return string[start:end+1]


if __name__ == '__main__':
    print longest_consecutive_substring('abcdefgdrrstqrstuvwxyzprr')
    print longest_consecutive_substring('abcdeddd ')
