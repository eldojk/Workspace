"""
amzn, msft

http://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-search-tree/
http://www.geeksforgeeks.org/find-distance-two-given-nodes/
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


"""
amzn
"""


def lca_bst(root, n1, n2):
    if root is None:
        return None

    if n1 > root.data and n2 > root.data:
        return lca(root.right, n1, n2)

    elif n1 < root.data and n2 < root.data:
        return lca(root.left, n1, n2)

    else:
        return root.data


def dist_from_root_bst(root, n, k):
    if root:
        if root.data > n:
            return dist_from_root_bst(root.left, n, k + 1)

        elif root.data < n:
            return dist_from_root_bst(root.right, n, k + 1)

        else:
            return k

    else:
        return -1


if __name__ == '__main__':
    print ''
    r = Node(3)
    r.left = Node(2)
    r.right = Node(4)
    r.left.left = Node(1)
    r.left.right = Node(2.5)
    r.right.left = Node(3.5)
    r.right.right = Node(7)

    print lca_bst(r, 2.5, 7)
    print dist_from_root_bst(r, 7, 0)


"""
amzn

http://www.geeksforgeeks.org/lowest-common-ancestor-in-a-binary-tree-set-2-using-parent-pointer/

2nd approach
"""


def depth(node):
    d = -1

    while node is not None:
        node = node.parent
        d += 1

    return d


def lca_with_parent_ptr(n1, n2):
    d1 = depth(n1)
    d2 = depth(n2)

    diff = abs(d1 - d2)

    a = n1
    b = n2

    if d1 > d2:
        a = n2
        b = n1

    # ^ a is the node at lesser depth

    while diff != 0:
        b = b.parent
        diff -= 1

    while a is not None and b is not None:
        if a == b:
            return a

        a = a.parent
        b = b.parent

    return None
