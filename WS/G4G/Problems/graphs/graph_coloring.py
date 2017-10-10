"""
http://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/
"""


def graph_color(graph):
    v = len(graph.keys())
    colors = [-1 for i in range(v)]
    available_colors = range(v)

    for u in graph.keys():
        if colors[u] == -1:
            for col in available_colors:
                if any([colors[neighbour] == col for neighbour in graph[u]]):
                    continue

                colors[u] = col
                break

            if colors[u] == -1:
                print 'Nope'
                return

    print colors


if __name__ == '__main__':
    g = {
        0: [1, 2],
        1: [0, 2, 3],
        2: [0, 1, 3],
        3: [1, 2, 4],
        4: [3]
    }
    graph_color(g)
