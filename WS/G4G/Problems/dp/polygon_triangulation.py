"""
http://www.geeksforgeeks.org/minimum-cost-polygon-triangulation/


Let Minimum Cost of triangulation of vertices from i to j be minCost(i, j)
If j < i + 2 Then
  minCost(i, j) = 0   # coz cost of triangulation of polygons having 1, 2 vertices is 0.
Else
  minCost(i, j) = Min { minCost(i, k) + minCost(k, j) + cost(i, k, j) }
                  Here k varies from 'i+1' to 'j-1'

Cost of a triangle formed by edges (i, j), (j, k) and (k, j) is
  cost(i, j, k)  = dist(i, j) + dist(j, k) + dist(k, j)

READ link for more desc
"""
from math import sqrt
from sys import maxint

from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def length(i, j, polygons):
    a = polygons[i][0]
    b = polygons[i][1]

    p = polygons[j][0]
    q = polygons[j][1]

    x = (a - p) ** 2
    y = (b - q) ** 2

    return sqrt(x + y)


def cost(i, j, k, polygons):
    return length(i, k, polygons) + length(j, k, polygons) + length(i, j, polygons)


def triangulation_cost(polygons):
    if len(polygons) <= 3:
        return 0

    dp = [[0 for i in polygons] for j in polygons]

    for l in range(len(polygons)):
        for i in range(len(polygons)):
            j = i + l

            if j < len(polygons):

                if j >= 2 + i:
                    dp[i][j] = maxint
                    for k in range(i + 1, j):
                        curr_cost = dp[i][k] + dp[k][j] + cost(i, j, k, polygons)
                        print i, j, k, curr_cost

                        if curr_cost < dp[i][j]:
                            dp[i][j] = curr_cost

    print_matrix(dp)


if __name__ == '__main__':
    pts = [(0, 0), (1, 0), (2, 1), (1, 2), (0, 2)]
    triangulation_cost(pts)
