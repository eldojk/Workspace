"""
amzn

https://www.quora.com/Given-the-position-x-y-of-a-knight-on-an-8X8-chess-board-what-is-the-probability-that-it-stays-within-the-chess-board-after-n-moves
"""


def is_in_board(x, y):
    # todo
    return True


def get_next_moves(x, y):
    # todo
    return []


def probablity(x, y, moves, memo):
    if not is_in_board(x, y):
        return 0

    if moves == 0:
        return 1

    if memo[x][y][moves] != -1:
        return memo[x][y][moves]

    ans = 0

    for coordinates in get_next_moves(x, y):
        ans += probablity(coordinates[0], coordinates[1], moves - 1, memo)

    memo[x][y][moves] = ans
    return ans

