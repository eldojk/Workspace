"""
http://www.geeksforgeeks.org/count-number-ways-reach-given-score-game/

Consider a game where a player can score 3 or 5 or 10 points in a move.
Given a total score n, find number of ways to reach the given score.

Examples:

Input: n = 20
Output: 4
There are following 4 ways to reach 20
(10, 10)
(5, 5, 10)
(5, 5, 5, 5)
(3, 3, 3, 3, 3, 5)

Input: n = 13
Output: 2
There are following 2 ways to reach 13
(3, 5, 5)
(3, 10)
"""


def num_ways(scor):
    dp = [0 for i in range(scor + 1)]

    dp[0] = 1

    for i in range(3, scor + 1):
        dp[i] += dp[i - 3]

    for i in range(5, scor + 1):
        dp[i] += dp[i - 5]

    for i in range(10, scor + 1):
        dp[i] += dp[i - 10]

    return dp[scor]


if __name__ == '__main__':
    print num_ways(20)
