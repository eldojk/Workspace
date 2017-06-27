"""
BACKTRACKING
amzn msft

http://www.geeksforgeeks.org/backtracking-set-7-suduku/
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def find_empty_location(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                return (i, j)

    return None


def is_used_in_row(board, r, c, num):
    for i in range(9):
        if board[r][i] == num:
            return True

    return False


def is_used_in_column(board, r, c, num):
    for i in range(9):
        if board[i][c] == num:
            return True

    return False


def used_in_box(board, r, c, num):
    for i in range(3):
        for j in range(3):
            if board[i + r][j + c] == num:
                return True

    return False


def is_safe(board, r, c, num):
    return not is_used_in_row(board, r, c, num) and \
           not is_used_in_column(board, r, c, num) and \
           not used_in_box(board, r - r % 3, c - c % 3, num)


def solve(board):
    loc = find_empty_location(board)

    if loc is None:
        return True

    r = loc[0]
    c = loc[1]

    for num in range(1, 10):
        if is_safe(board, r, c, num):
            board[r][c] = num

            if solve(board):
                return True

            board[r][c] = 0

    return False


if __name__ == '__main__':
    grid = [[3, 0, 6, 5, 0, 8, 4, 0, 0],
            [5, 2, 0, 0, 0, 0, 0, 0, 0],
            [0, 8, 7, 0, 0, 0, 0, 3, 1],
            [0, 0, 3, 0, 1, 0, 0, 8, 0],
            [9, 0, 0, 8, 6, 3, 0, 0, 5],
            [0, 5, 0, 0, 9, 0, 6, 0, 0],
            [1, 3, 0, 0, 0, 0, 2, 5, 0],
            [0, 0, 0, 0, 0, 0, 0, 7, 4],
            [0, 0, 5, 2, 0, 6, 3, 0, 0]]

    if solve(grid):
        print_matrix(grid)

    else:
        print 'Nope'