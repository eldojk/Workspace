"""
http://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
"""


class Node(object):
    def __init__(self, data):
        self.left = None
        self.right = None
        self.data = data

    def __repr__(self):
        return str(self.data)


def lca(root, n1, n2):
    if root is None:
        return None

    if root.data == n1 or root.data == n2:
        return root

    left_lca = lca(root.left, n1, n2)
    right_lca = lca(root.right, n1, n2)

    if left_lca is not None and right_lca is not None:
        return root

    return left_lca if right_lca is None else right_lca


def dist(root, n1, curr):
    if root is None:
        return 0

    if root.data == n1:
        return curr

    l_d = dist(root.left, n1, curr + 1)
    r_d = dist(root.right, n1, curr + 1)

    return l_d if l_d > 0 else r_d


def dist_bw_nodes(root, n1, n2):
    n1dist = dist(root, n1, 0)
    n2dist = dist(root, n2, 0)
    lca_node = lca(root, n1, n2)
    lca_dist = dist(root, lca_node.data, 0)

    return n1dist + n2dist - (2 * lca_dist)


if __name__ == '__main__':
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    r.right.left = Node(6)
    r.right.right = Node(7)

    print lca(r, 3, 4)
    print ''
    print dist(r, 4, 0)
    print dist(r, 3, 0)
    print ''
    print dist_bw_nodes(r, 4, 5)
    print dist_bw_nodes(r, 3, 4)
