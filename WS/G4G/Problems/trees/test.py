from sys import maxint

from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def is_valid(i, j, r, c):
    return 0 <= i < r and 0 <= j < c


def __find(m, dp, i, j, r, c, dir):
    if not is_valid(i, j, r, c) or m[i][j] == '#':
        return 0

    if dp[i][j][dir] != -1:
        return dp[i][j][dir]

    res = 1 if m[i][j] == 'C' else 0

    if dir == 0:
        res += max(
            __find(m, dp, i + 1, j, r, c, 1),
            __find(m, dp, i, j - 1, r, c, 0)
        )
    elif dir == 1:
        res += max(
            __find(m, dp, i + 1, j, r, c, 0),
            __find(m, dp, i, j + 1, r, c, 1)
        )

    dp[i][j][dir] = res
    return dp[i][j][dir]


def find_max_coins(m):
    r = len(m)
    c = len(m[0])
    dp = [[[-1 for i in ['l', 'r']] for j in range(c)] for k in range(r)]

    return __find(m, dp, 0, 0, r, c, 1)


if __name__ == '__main__':
    m = [
        ['E', 'C', 'C', 'C', 'C'],
        ['C', '#', 'C', '#', 'E'],
        ['#', 'C', 'C', '#', 'C'],
        ['C', 'E', 'E', 'C', 'E'],
        ['C', 'E', '#', 'C', 'E']
    ]
    print find_max_coins(m)
