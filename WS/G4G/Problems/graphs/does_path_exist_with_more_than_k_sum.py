"""
http://www.geeksforgeeks.org/find-if-there-is-a-path-of-more-than-k-length-from-a-source/
"""


def is_path_exists(g, source, k, hm):
    if k <= 0:
        return True

    hm[source] = True

    for neighbour, dist in g[source]:
        if hm.get(neighbour):
            continue

        if dist >= k:
            return True

        hm[neighbour] = True

        if is_path_exists(g, neighbour, k - dist, hm):
            return True

        hm.pop(neighbour)

    return False

