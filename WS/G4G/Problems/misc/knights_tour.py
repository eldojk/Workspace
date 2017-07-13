"""
BACKTRACKING
amzn msft

http://www.geeksforgeeks.org/backtracking-set-1-the-knights-tour-problem/
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def is_safe_move(x, y, solution, n):
    return 0 <= x < n and 0 <= y < n and solution[x][y] == -1


def solve_recur(x, y, curr_move, x_move, y_move, solution):
    if curr_move == 8*8:
        return True

    for i in range(8):
        next_x = x + x_move[i]
        next_y = y + y_move[i]

        if is_safe_move(next_x, next_y, solution, 8):
            solution[next_x][next_y] = curr_move

            if solve_recur(next_y, next_y, curr_move + 1, x_move, y_move, solution):
                return True

            else:
                solution[next_x][next_y] = -1

    return False


def solve():
    solution = [[-1 for i in range(8)] for j in range(8)]

    x_move = [2, 1, -1, -2, -2, -1,  1,  2]
    y_move = [1, 2,  2,  1, -1, -2, -2, -1]

    solution[0][0] = 0

    if not solve_recur(0, 0, 1, x_move, y_move, solution):
        print 'Nope'
        return

    else:
        print_matrix(solution)


if __name__ == '__main__':
    solve()
