"""
http://www.geeksforgeeks.org/find-the-minimum-cost-to-reach-a-destination-where-every-station-is-connected-in-one-direction/

There are N stations on route of a train. The train goes from station 0 to N-1.
The ticket cost for all pair of stations (i, j) is given where j is greater than i.
Find the minimum cost to reach the destination.

Consider the following example:

Input:
cost[N][N] = { {0, 15, 80, 90},
              {INF, 0, 40, 50},
              {INF, INF, 0, 70},
              {INF, INF, INF, 0}
             };

Output:
The minimum cost is 65
The minimum cost can be obtained by first going to station 1
from 0. Then from station 1 to station 3.

recurrence (different from g4g's implementation
min_cost(0, n - 1) = min(
                        c[0][n-1],
                        min_cost(0, n - 2) + c[n-2][n-1],
                        min_cost(0, n - 3) + min_cost(n-3, n-1) ...)
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def find_min_cost(cost):
    min_cost = [[0 for i in cost] for j in cost]

    # base case, for 1,2 .. 2, 3 .. 3, 4 etc
    for i in range(1, len(min_cost)):
        min_cost[i - 1][i] = cost[i - 1][i]

    for l in range(2, len(min_cost)):
        for i in range(len(min_cost)):

            j = i + l

            if j < len(min_cost):
                min_cost[i][j] = cost[i][j]  # using the first option, 1-2, 2-3, 3-4 ...

                for k in range(i + 1, j):
                    min_cost[i][j] = min(
                        min_cost[i][j],
                        (min_cost[i][k] + min_cost[k][j])  # choosing intermediate stops and minimising
                    )

    # print_matrix(min_cost)
    return min_cost[0][len(min_cost) - 1]


if __name__ == '__main__':
    c = [
        [0, 15, 80, 90],
        [0, 0, 40, 50],
        [0, 0, 0, 70],
        [0, 0, 0, 0]
    ]

    print find_min_cost(c)
