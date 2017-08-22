# coding=utf-8
"""
amzn

http://www.geeksforgeeks.org/minimum-positive-points-to-reach-destination/

We can solve this problem through bottom-up table filling dynamic programing technique.

To begin with, we should maintain a 2D array dp of the same size as the grid, where dp[i][j] represents the minimum
points that guarantees the continuation of the journey to destination before entering the cell (i, j). It’s but obvious
that dp[0][0] is our final solution. Hence, for this problem, we need to fill the table from the bottom right corner to
left top.
Now, let us decide minimum points needed to leave cell (i, j) (remember we are moving from bottom to up). There are only
two paths to choose: (i+1, j) and (i, j+1). Of course we will choose the cell that the player can finish the rest of his
journey with a smaller initial points. Therefore we have: min_Points_on_exit = min(dp[i+1][j], dp[i][j+1])
Now we know how to compute min_Points_on_exit, but we need to fill the table dp[][] to get the solution in dp[0][0].

How to compute dp[i][j]?
     The value of dp[i][j] can be written as below.

dp[i][j] = max(min_Points_on_exit – points[i][j], 1)

Let us see how above expression covers all cases.

If points[i][j] == 0, then nothing is gained in this cell; the player can leave the cell with the same points as he
enters the room with, i.e. dp[i][j] = min_Points_on_exit.
If dp[i][j] < 0, then the player must have points greater than min_Points_on_exit before entering (i, j) in order to
compensate for the points lost in this cell. The minimum amount of compensation is " - points[i][j] ", so we have
dp[i][j] = min_Points_on_exit - points[i][j].
If dp[i][j] > 0, then the player could enter (i, j) with points as little as min_Points_on_exit – points[i][j]. since he
could gain “points[i][j]” points in this cell. However, the value of min_Points_on_exit – points[i][j] might drop to 0
or below in this situation. When this happens, we must clip the value to 1 in order to make sure dp[i][j] stays
positive: dp[i][j] = max(min_Points_on_exit – points[i][j], 1).

Finally return dp[0][0] which is our answer.
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def min_initial_pts(points):
    dp = [[0 for i in points[0]] for j in points]
    m = len(dp)
    n = len(dp[0])

    dp[m - 1][n - 1] = 1 if points[m - 1][n - 1] > 0 else abs(points[m - 1][n - 1]) + 1

    i = m - 2
    while i >= 0:
        dp[i][n - 1] = max(dp[i + 1][n - 1] - points[i][n - 1], 1)
        i -= 1

    j = n - 2
    while j >= 0:
        dp[m - 1][j] = max(dp[m - 1][j + 1] - points[m - 1][j], 1)
        j -= 1

    i = m - 2

    while i >= 0:

        j = n - 2
        while j >= 0:
            min_pts_on_exit = min(dp[i + 1][j], dp[i][j + 1])
            dp[i][j] = max(min_pts_on_exit - points[i][j], 1)

            j -= 1

        i -= 1

    # print_matrix(dp)
    return dp[0][0]


if __name__ == '__main__':
    m = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]
    print min_initial_pts(m)
