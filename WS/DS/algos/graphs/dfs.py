"""
Depth first search
"""


def DFS(graph, source):
    source.predecessor = None
    source.distance = 0
    source.is_visited = True
    do_dfs(graph, source)


def do_dfs(graph, node):
    for neighbour in graph[node]:
        if not neighbour.is_visited:
            neighbour.is_visited = True
            neighbour.predecessor = node
            neighbour.distance = node.distance + 1
            do_dfs(graph, neighbour)
