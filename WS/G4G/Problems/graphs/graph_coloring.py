"""
http://www.geeksforgeeks.org/graph-coloring-set-2-greedy-algorithm/
"""


def color(v, colors, available_colors, unusable_colors):
    for col in available_colors:
        if col not in unusable_colors:
            colors[v] = col
            return


def graph_color(graph):
    v = len(graph.keys())
    colors = [-1 for i in range(v)]
    available_colors = range(v)

    colors[0] = 0

    for u in graph.keys():
        for v in graph[u]:
            if colors[v] == -1:
                unusable_colors = [colors[i] for i in graph[u] if colors[i] != -1]
                unusable_colors += [colors[i] for i in graph[v] if colors[i] != -1]
                color(v, colors, available_colors, unusable_colors)

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
