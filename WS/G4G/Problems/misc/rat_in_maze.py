"""
BACKRACKING SOLUTION
amzn

http://www.geeksforgeeks.org/backttracking-set-2-rat-in-a-maze/
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def is_safe(x, y, n, visited, matrix):
    return 0 <= x < n and 0 <= y < n and (visited[x][y] != 1) and matrix[x][y] == 1


def is_rat_reached_dest(matrix, x, y, n, visited):
    if x == y == n - 1:
        return True

    x_moves = [0, 1]
    y_moves = [1, 0]

    for i in range(2):
        next_x = x_moves[i] + x
        next_y = y_moves[i] + y

        if is_safe(next_x, next_y, n, visited, matrix):

            visited[next_x][next_y] = 1

            if is_rat_reached_dest(matrix, next_x, next_y, n, visited):
                return True

            else:
                visited[next_x][next_y] = 0

    return False


def solve(matrix):
    visited = [[0 for i in matrix] for j in matrix]
    visited[0][0] = 1

    ans = is_rat_reached_dest(matrix, 0, 0, len(matrix), visited)
    if ans:
        print_matrix(visited)

    return ans


if __name__ == '__main__':
    print solve(
        [
            [1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [1, 1, 1, 1]
        ]
    )
