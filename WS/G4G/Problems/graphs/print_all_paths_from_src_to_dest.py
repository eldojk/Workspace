"""
amzn

http://www.geeksforgeeks.org/find-paths-given-source-destination/
"""


def print_all_paths(s, d, visited, path, graph):
    visited[s] = True
    path.append(s)

    if s == d:
        print ' '.join(map(str, path))

    else:
        for neighbour in graph[s]:
            if not visited[neighbour]:
                print_all_paths(neighbour, d, visited, path, graph)

    visited[s] = False
    path.pop()