# coding=utf-8
"""
http://www.geeksforgeeks.org/mobile-numeric-keypad-problem/

Given the mobile numeric keypad. You can only press buttons that are up, left, right or down to the current button. You
are not allowed to press bottom row corner buttons (i.e. * and # ).
Given a number N, find out the number of possible numbers of given length.

Examples:
For N=1, number of possible numbers would be 10 (0, 1, 2, 3, …., 9)
For N=2, number of possible numbers would be 36
Possible numbers: 00,08 11,12,14 22,21,23,25 and so on.

N = 1 is trivial case, number of possible numbers would be 10 (0, 1, 2, 3, …., 9)
For N > 1, we need to start from some button, then move to any of the four direction (up, left, right or down) which
takes to a valid button (should not go to *, #). Keep doing this until N length number is obtained
(depth first traversal).

count(i, N) -> number of possible combinations of len N starting with digit i

count(i, N) = sum (count(j, N-1) ) where j is all the positions from which i can be reached in one move

total count = sum(count(i, n) for i in 0 to 9)
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


KEY_PAD = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [None, 0, None]
]


def is_valid(move):
    i = move[0]
    j = move[1]

    if i != 3:
        return 0 <= i < 3 and 0 <= j < 3

    return i == 3 and j == 1


def get_moves(i, j):
    moves = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1), (i, j)]

    return [m for m in moves if is_valid(m)]


def get_count(n):
    global KEY_PAD

    dp = [[0 for i in range(10)] for j in range(n + 1)]

    # count numbers starting with digit i and of lengths 0 and 1
    for i in range(10):
        dp[0][i] = 0
        dp[1][i] = 1

    for k in range(2, n + 1):

        # all keys
        for i in range(4):
            for j in range(3):

                if KEY_PAD[i][j] is not None:

                    # the valid moves I can make from i j are same as those places from where i can reach back i j from
                    moves = get_moves(i, j)

                    # sum over all such places from where i, j can be reached
                    for move in moves:
                        r = move[0]
                        c = move[1]

                        neighbour = KEY_PAD[r][c]
                        num = KEY_PAD[i][j]

                        dp[k][num] += dp[k - 1][neighbour]

    # print_matrix(dp)
    return sum(dp[n])  # sum of all possible moves with length n


if __name__ == '__main__':
    print get_count(5)
