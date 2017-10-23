from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def is_valid(x, y, n):
    if (0 <= x < n) and (0 <= y < n):
        return n > y >= (n - 1 - x)

    return False


def get_paths(i, j, dp, n):
    if i == 0 and j == n - 1:
        return 1

    if dp[i][j] != -1:
        return dp[i][j]

    dp[i][j] = 0
    neighbours = [(i - 1, j), (i, j + 1)]

    for neighbour in neighbours:
        x = neighbour[0]
        y = neighbour[1]
        if is_valid(x, y, n):
            print x, y
            dp[i][j] += get_paths(x, y, dp, n)

    return dp[i][j]


def num_of_paths_to_dest(n):
    dp = [[-1 for i in range(n)] for j in range(n)]
    v = get_paths(n - 1, 0, dp, n)
    print_matrix(dp)
    return v


if __name__ == '__main__':
    print num_of_paths_to_dest(4)