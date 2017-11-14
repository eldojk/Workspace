"""
amzn

http://www.geeksforgeeks.org/collect-maximum-coins-before-hitting-a-dead-end/

maxCoins(i, j, d):  Maximum number of coins that can be
                    collected if we begin at cell (i, j)
                    and direction d.
                    d can be either 0 (left) or 1 (right)

   // If this is a blocking cell, return 0. isValid() checks
   // if i and j are valid row and column indexes.
   If (arr[i][j] == '#' or isValid(i, j) == false)
       return 0

   // Initialize result
   If (arr[i][j] == 'C')
       result = 1;
   Else
       result = 0;

   If (d == 0) // Left direction
       return result +  max(maxCoins(i+1, j, 1),  // Down
                            maxCoins(i, j-1, 0)); // Ahead in left

   If (d == 1) // Right direction
       return result +  max(maxCoins(i+1, j, 0),  // Down
                            maxCoins(i, j+1, 1)); // Ahead in right
"""


def is_valid(i, j, r, c):
    return 0 <= i < r and 0 <= j < c


def _find_max(matrix, r, c, dp, i, j, direction):
    if not is_valid(i, j, r, c) or matrix[i][j] == '#':
        return 0

    if dp[i][j][direction] != -1:
        return dp[i][j][direction]

    if matrix[i][j] == 'C':
        result = 1
    else:
        result = 0

    if direction == 0:  # left
        result += max(
            _find_max(matrix, r, c, dp, i + 1, j, 1),  # go down and right
            _find_max(matrix, r, c, dp, i, j - 1, 0)  # go left
        )
    elif direction == 1:
        result += max(
            _find_max(matrix, r, c, dp, i + 1, j, 0),  # go down and left
            _find_max(matrix, r, c, dp, i, j + 1, 1)  # go right
        )

    dp[i][j][direction] = result

    return dp[i][j][direction]


def find_max_coins(matrix):
    r = len(matrix)
    c = len(matrix[0])

    dp = [[[-1 for i in ('left', 'right')] for j in range(c)] for k in range(r)]

    return _find_max(matrix, r, c, dp, 0, 0, 1)


if __name__ == '__main__':
    m = [
        ['E', 'C', 'C', 'C', 'C'],
        ['C', '#', 'C', '#', 'E'],
        ['#', 'C', 'C', '#', 'C'],
        ['C', 'E', 'E', 'C', 'E'],
        ['C', 'E', '#', 'C', 'E']
    ]
    print find_max_coins(m)
