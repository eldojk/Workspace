"""
amzn

http://www.geeksforgeeks.org/fill-array-1s-minimum-iterations-filling-neighbors/

using bfs
"""
from Queue import Queue


def find_min_iterations(array):
    q = Queue()
    n = len(array)
    res = 0

    for i in range(n):
        if array[i] == 1:
            q.put((i, 0))

    while not q.empty():
        el = q.get()
        j = el[0]
        dist = el[1]
        res = max(res, dist)

        if j + 1 < n and array[j + 1] == 0:
            q.put((j + 1, dist + 1))
            array[j + 1] = 1

        if j - 1 >= 0 and array[j - 1] == 0:
            q.put((j - 1, dist + 1))
            array[j - 1] = 1

    return dist


if __name__ == '__main__':
    print find_min_iterations([1, 0, 1, 0, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1])
    print find_min_iterations([0, 0, 1, 1, 0, 0, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 1])