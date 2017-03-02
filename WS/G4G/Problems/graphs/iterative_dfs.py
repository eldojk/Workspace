"""
http://www.geeksforgeeks.org/iterative-depth-first-traversal/
"""
from G4G.Problems.stacks.stack import Stack


def iterative_dfs(graph, source):
    s = Stack()
    s.push(source)
    visited = [False for i in graph.keys()]

    while not s.is_empty():
        node = s.pop()

        visited[node] = True

        for neighbour in graph[node]:
            if not visited[neighbour]:
                s.push(neighbour)
