# coding=utf-8
"""
http://www.geeksforgeeks.org/count-possible-paths-source-destination-exactly-k-edges/ (READ RECURSIVE IMPLEMENTATION
HERE)

Given a directed graph and two vertices ‘u’ and ‘v’ in it, count all possible walks from ‘u’ to ‘v’ with exactly k edges
on the walk.

The graph is given as adjacency matrix representation where value of graph[i][j] as 1 indicates that there is an edge
from vertex i to vertex j and a value 0 indicates no edge from i to j.

recursive
// Go to all adjacents of u and recur
        for (int i = 0; i < V; i++)
            if (graph[u][i] == 1)  // Check if is adjacent of u
                count += countwalks(graph, i, v, k-1);

The idea is:
num walks from u to v using k edges = sum ( num walks using i to v using k - 1 edges, for all i adjacent to u)
"""
from G4G.Problems.dp.min_matrix_cost_path_to_mn import print_matrix


def num_walks(graph, u, v, k):
    dp = [[0 for i in range(k + 1)] for j in range(len(graph))]

    # base cases
    # k = 0 -> only one way to get to v using 0 edges is when source == v
    dp[v][0] = 1

    # k = 1 -> i.e. for all vertices with one edge to v
    for i in range(len(graph)):
        if graph[i][v] == 1:  # there is an edge from i to v
            dp[i][1] = 1  # i to 1 using one edge

    for i in range(len(graph)):
        for j in range(2, k + 1):

            for m in range(len(graph)):
                if graph[i][m] == 1:  # if a edge exists from i to m
                    dp[i][j] += dp[m][j - 1]  # i to v using j steps += m to v using k - 1 steps

    # print_matrix(dp)
    return dp[u][k]


if __name__ == '__main__':
    g = [
        [0, 1, 1, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 1],
        [0, 0, 0, 0]
    ]

    print num_walks(g, 0, 3, 2)


"""
To get length of shortest walk with exactly k edges, find minimum of all edges
dp[i][j] = min( dp[m][j - 1] + graph[i][m]) for m in V if m != i.

# graph[a][b] = n if n is the weight of edge between a and b
"""
