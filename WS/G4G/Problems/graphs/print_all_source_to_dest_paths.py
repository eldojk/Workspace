"""
http://www.geeksforgeeks.org/find-paths-given-source-destination/
"""


def print_all_paths(graph, visited, path, v, d):
    visited[v] = True
    path.append(v)

    if v == d:
        print path

    else:
        for neighbour in graph[v]:
            if not visited[neighbour]:
                print_all_paths(graph, visited, path, neighbour, d)

    path.pop()
    visited[v] = False


if __name__ == '__main__':
    g = {
        0: [2, 1, 3],
        1: [3],
        2: [0, 1],
        3: []
    }
    visited = [False for i in range(len(g.keys()))]

    print_all_paths(g, visited, [], 2, 3)
