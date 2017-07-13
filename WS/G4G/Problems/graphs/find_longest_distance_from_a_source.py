"""
amzn

backtracking

Given a equi-weighted uni directed graph and need to find the max distance possible from a given node
"""
from sys import maxint


DIST = -maxint


def get_longest_dist(graph, source, visited, curr_dist):
    global DIST
    visited[source] = True

    if curr_dist > DIST:
        DIST = curr_dist

    for neighbour in graph[source]:
        if not visited[neighbour]:
            get_longest_dist(graph, neighbour, visited, curr_dist + 1)

    visited[source] = False


if __name__ == '__main__':
    g = {
        0: [1, 2, 3],
        1: [0],
        2: [0, 3],
        3: [0, 2]
    }

    visited = [False for i in range(4)]
    get_longest_dist(g, 0, visited, 0)
    print DIST