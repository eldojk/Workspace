# coding=utf-8
"""
amzn

We can solve this problem through bottom-up table filling dynamic programing technique.

To begin with, we should maintain a 2D array dp of the same size as the grid, where dp[i][j]
represents the minimum points that guarantees the continuation of the journey to destination
before entering the cell (i, j). It’s but obvious that dp[0][0] is our final solution.
Hence, for this problem, we need to fill the table from the bottom right corner to left top.
Now, let us decide minimum points needed to leave cell (i, j)
(remember we are moving from bottom to up). There are only two paths to choose: (i+1, j)
and (i, j+1). Of course we will choose the cell that the player can finish the rest
of his journey with a smaller initial points.
Therefore we have: min_Points_on_exit = min(dp[i+1][j], dp[i][j+1])
Now we know how to compute min_Points_on_exit, but we need to fill the table dp[][]
to get the solution in dp[0][0].

How to compute dp[i][j]?
     The value of dp[i][j] can be written as below.

dp[i][j] = max(min_Points_on_exit – points[i][j], 1)


Let us see how above expression covers all cases.

If points[i][j] == 0, then nothing is gained in this cell; the player can leave
the cell with the same points as he enters the room with, i.e. dp[i][j] = min_Points_on_exit.
If dp[i][j] < 0, then the player must have points greater than min_Points_on_exit
before entering (i, j) in order to compensate for the points lost in this cell.
The minimum amount of compensation is " - points[i][j] ",
so we have dp[i][j] = min_Points_on_exit - points[i][j].
If dp[i][j] > 0, then the player could enter (i, j) with points as little as
min_Points_on_exit – points[i][j]. since he could gain “points[i][j]” points in this cell.
However, the value of min_Points_on_exit – points[i][j] might drop to 0 or below in this
situation. When this happens, we must clip the value to 1 in order to
make sure dp[i][j] stays positive:
dp[i][j] = max(min_Points_on_exit – points[i][j], 1).
Finally return dp[0][0] which is our answer.

Somethings maybe written clearly though:
1. We can not use top left to bottom right DP because we cannot guarantee the min points at each cell.
Only by using the information from (i+1,j) and (i,j+1) can we decide that. Hence reverse procedure.
We assign the min value possible for (m-1,n-1) cell.
2. dp[i][j] represents the min points needed to continue the journey from (i,j). Firstly it must
be atleast 1. Also we may go to (i+1,j) from here or (i,j+1) and we already know the min points
needed to reach the end from both of them. So take minimum and we may gain or lose point on (i,j)
compensate for that too. Remember minimum points needed to enter may be less but we have a
restriction to have at least 1 point.
"""


def min_points(points):
    r = len(points)
    c = len(points[0])

    dp = [[0 for i in range(c)] for j in range(r)]

    dp[r - 1][c - 1] = 1 if points[r - 1][c - 1] > 0 else 1 + abs(points[r - 1][c - 1])

    # fill last col and last row. since only one type of
    # move is possible (down or right)
    i = r - 2
    while i >= 0:
        dp[i][c - 1] = max(dp[i + 1][c - 1] - points[i][c - 1], 1)
        i -= 1

    j = c - 2
    while j >= 0:
        dp[c - 1][j] = max(dp[c - 1][j + 1] - points[c - 1][j], 1)
        j -= 1

    i = r - 2
    while i >= 0:
        j = c - 2

        while j >=0:
            min_pts_on_exit = min(
                dp[i + 1][j],
                dp[i][j + 1]
            )
            dp[i][j] = max(min_pts_on_exit - points[i][j], 1)

            j -= 1

        i -= 1

    return dp[0][0]


if __name__ == '__main__':
    m = [
        [-2, -3, 3],
        [-5, -10, 1],
        [10, 30, -5]
    ]
    print min_points(m)
