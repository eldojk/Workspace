"""
BACKRACKING SOLUTION
amzn

http://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/
"""


def is_safe(x, y, n, visited):
    return 0 <= x < n and 0 < y < n and not visited[x][y]


def is_rat_reached_dest(matrix, x, y, n, visited):
    if x == y == n - 1:
        return True

    x_moves = [0, 1]
    y_moves = [1, 0]

    for i in range(2):
        next_x = x_moves[i] + x
        next_y = y_moves[i] + y

        if is_safe(next_x, next_y, n, visited):

            visited[next_x][next_y] = True

            if is_rat_reached_dest(matrix, next_x, next_y, n, visited):
                return True

            else:
                visited[next_x][next_y] = False

    return False


def solve(matrix):
    visited = [[False for i in matrix] for j in matrix]
    visited[0][0] = True

    return is_rat_reached_dest(matrix, 0, 0, len(matrix), visited)


if __name__ == '__main__':
    print solve(
        [
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]
        ]
    )