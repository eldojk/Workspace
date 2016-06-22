"""
Breadth first search
"""
from Queue import Queue


def visit(node, _from, distance):
    if not node.is_visited:
        node.distance = distance
        node.predecessor = _from
        node.set_visited()


def do_bfs(graph, source):
    q = Queue()
    source.distance = 0
    source.predecessor = None
    q.put(source)

    while not q.empty():
        node = q.get()

        for neighbour in graph[node]:
            if not neighbour.is_visited:
                neighbour.predecessor = node
                neighbour.distance = node.distance + 1
                q.put(neighbour)

        node.set_visited()
