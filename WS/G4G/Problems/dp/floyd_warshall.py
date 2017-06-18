"""
msft

http://www.geeksforgeeks.org/dynamic-programming-set-16-floyd-warshall-algorithm/
"""
from sys import maxint


def all_pair_shortest_path(graph):
    n = len(graph)
    dp = [[0 for i in n] for j in n]

    for i in range(n):
        for j in range(n):
            dp[i][j] = graph[i][j] if graph[i][j] != 0 else maxint

    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dp[i][k] + dp[k][j] < dp[i][j]:
                    dp[i][j] = dp[i][k] + dp[k][j]

    return dp
