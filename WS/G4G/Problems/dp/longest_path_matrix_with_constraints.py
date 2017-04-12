"""
http://www.geeksforgeeks.org/find-the-longest-path-in-a-matrix-with-given-constraints/

Input:  mat[][] = {{1, 2, 9}
                   {5, 3, 8}
                   {4, 6, 7}}
Output: 4
The longest path is 6-7-8-9.

The idea is simple, we calculate longest path beginning with every cell. Once we have computed longest for all cells,
we return maximum of all longest paths.
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def get_valid_neighbours(i, j, matrix):
    m = len(matrix)
    neighbours = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]

    v_n = []
    for n in neighbours:
        p = n[0]
        q = n[1]

        if 0 <= p < m and 0 <= q < m and (matrix[i][j] + 1 == matrix[p][q]):  # validation condition fo valid next el
            v_n.append(n)

    return v_n


def dfs(matrix, dp, i, j, visited):
    print 'dfs'
    visited[i][j] = True  # setting this flag so that we don't come back here in this dfs recursion

    if dp[i][j] != -1:
        return dp[i][j]

    for n in get_valid_neighbours(i, j, matrix):
        p = n[0]
        q = n[1]
        if not visited[p][q]:
            dp[i][j] = 1 + dfs(matrix, dp, p, q, visited)
            visited[i][j] = False  # unset for further use
            return dp[i][j]

    visited[i][j] = False  # unset for further use
    dp[i][j] = 1  # include that element only, hence length one
    return dp[i][j]


def longest_len_path(matrix):
    dp = [[-1 for i in matrix] for j in matrix]
    visited = [[False for i in matrix] for j in matrix]

    result = 1
    for i in range(len(matrix)):
        for j in range(len(matrix)):

            if dp[i][j] == -1:
                dfs(matrix, dp, i, j, visited)  # doing dfs to find neighbours

            result = max(result, dp[i][j])  # store maximum such result

    # print_matrix(dp)
    return result


if __name__ == '__main__':
    m = [
        [1, 2, 9],
        [5, 3, 8],
        [4, 6, 7]
    ]
    print longest_len_path(m)
