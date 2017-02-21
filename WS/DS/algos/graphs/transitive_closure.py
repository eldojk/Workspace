"""
http://www.geeksforgeeks.org/transitive-closure-of-a-graph-using-dfs/
"""


TRANSITIVE_CLOSURE = None
VISITED = None


def dfs(graph, v, source):
    global VISITED
    VISITED[v] = True
    TRANSITIVE_CLOSURE[source][v] = 1

    for neighbour in graph[v]:
        if not VISITED[neighbour]:
            dfs(graph, neighbour, source)


def find_transititve_closure(graph):
    global TRANSITIVE_CLOSURE, VISITED
    vertices = graph.keys()
    num_vertices = len(vertices)

    TRANSITIVE_CLOSURE = [[0 for i in vertices] for j in vertices]

    for vertex in vertices:
        VISITED = [False for v in vertices]
        dfs(graph, vertex, vertex)

    for row in TRANSITIVE_CLOSURE:
        print " ".join(map(str, row))


if __name__ == '__main__':
    graph_to_compute = {
        0: [1, 2],
        1: [2],
        2: [0, 3],
        3: []
    }

    find_transititve_closure(graph_to_compute)
