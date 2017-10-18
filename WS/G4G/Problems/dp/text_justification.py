"""
mit - https://www.youtube.com/watch?v=ENyox7kNKeY
tushar - https://www.youtube.com/watch?v=RORuwHiblPc

badness(i, j) = INF if they don't fit
                (page width - total width)^3

using badness(i,j) for dp
dp[i] = where the word should be split (i to dp[i]), not including the value at dp[i]
dp[i] = for j in i+1 to n:
			min(dp[j] + badness(i, j-1))

cost
0	1	2	3	4
26	10	34	9	36

dp[i]
0	1	2	3	4
1	3	3	5	5
"""
from sys import maxint

from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def compute_chars(words, i, j):
    chars = len(words[i])

    for k in range(i+1, j+1):
        chars += 1 + len(words[k])

    return chars


def compute_badness(words, width):
    badness = [[maxint for i in words] for j in words]

    for i in range(len(words)):
        for j in range(i, len(words)):

            chars = compute_chars(words, i, j)
            if chars > width:
                break
            else:
                badness[i][j] = (width - chars)**2

    return badness


def minimise_badness(words, width):
    badness = compute_badness(words, width)

    cost = [maxint for i in words] + [0]
    dp = [0 for i in words]

    i = len(words) - 1
    while i >= 0:
        j = len(words)
        cost[i] = badness[i][j - 1]
        dp[i] = len(words)

        while j > i:
            if badness[i][j - 1] == maxint:
                j -= 1
                continue
            if cost[i] > cost[j] + badness[i][j - 1]:
                cost[i] = cost[j] + badness[i][j - 1]
                dp[i] = j

            j -= 1

        i -= 1

    print_matrix(badness)
    print dp
    print cost


if __name__ == '__main__':
    minimise_badness(['tushar', 'roy', 'likes', 'to', 'code'], 10)
