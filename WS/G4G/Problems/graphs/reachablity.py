"""
In a Directed graph find if a node a is reachable from another node b
"""


def is_reachable(node1, node2, graph):
    dfs(node1, graph)

    return node2.is_visited


def dfs(source, graph):
    source.is_visited = True
    for neighbour in graph[source]:
        if not neighbour.is_visited:
            dfs(neighbour, graph)