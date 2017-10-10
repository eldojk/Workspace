"""
amzn, msft

http://www.geeksforgeeks.org/minimum-steps-reach-target-knight/

do bfs
"""
from Queue import Queue


def is_valid(x, y, m, n):
    return 0 <= x < m and 0 <= y < n


def get_neighbours(x, y, m, n):
    dx = [2, -2, 2, -2, 1, -1, 1, -1]
    dy = [1, 1, -1, -1, 2, 2, -2, -2]
    neighbours = []

    for i in range(8):
        a = x + dx[i]
        b = y + dy[i]

        if is_valid(a, b, m, n):
            neighbours.append((a, b))

    return neighbours


def get_min_steps_to_target(m, n, x, y, p, q):
    queue = Queue()
    visited = [[False for i in range(n)] for j in range(m)]
    queue.put((x, y, 0))
    visited[x][y] = True

    while not queue.empty():
        pair = queue.get()
        x = pair[0]
        y = pair[1]
        dist = pair[2]

        if x == p and y == q:
            return dist

        for neighbour in get_neighbours(x, y, m, n):
            a = neighbour[0]
            b = neighbour[1]

            if not visited[a][b]:
                queue.put((a, b, dist + 1))

    return "infinity"


if __name__ == '__main__':
    print get_min_steps_to_target(6, 6, 4, 5, 1, 1)
