"""
http://www.geeksforgeeks.org/find-closest-leaf-binary-tree/
"""
from sys import maxint
from G4G.Problems.bst.vertical_sum import Node


def is_leaf(node):
    return node.left is None and node.right is None


CLOSEST_LEAF = None
CLOSEST_LEAF_DIST = maxint


def update_closest_leaf(node, dist):
    global CLOSEST_LEAF, CLOSEST_LEAF_DIST
    if node is None:
        return

    if is_leaf(node):
        if dist < CLOSEST_LEAF_DIST:
            CLOSEST_LEAF = node
            CLOSEST_LEAF_DIST = dist

    update_closest_leaf(node.left, dist + 1)
    update_closest_leaf(node.left, dist + 1)


def closest_leaf(root, node):
    if root is None:
        return False, -1

    if root == node:
        update_closest_leaf(node, 0)
        return True, 1

    is_found_left, l_dist = closest_leaf(root.left, node)
    is_found_right, r_dist = closest_leaf(root.right, node)

    dist = -1
    if is_found_left:
        dist = l_dist + 1
        update_closest_leaf(root.right, dist)

    if is_found_right:
        dist = r_dist + 1
        update_closest_leaf(root.left, dist)

    return is_found_left or is_found_right, dist


if __name__ == '__main__':
    r = Node('A')
    r.left = Node('B')
    r.right = Node('C')
    r.right.left = Node('E')
    r.right.right = Node('F')
    r.right.left.left = Node('G')
    r.right.right.right = Node('H')
    r.right.left.left.left = Node('I')
    r.right.left.left.right = Node('J')
    r.right.right.right.left = Node('K')

    closest_leaf(r, r.right.right.right)
    print CLOSEST_LEAF

    CLOSEST_LEAF = None
    CLOSEST_LEAF_DIST = maxint

    closest_leaf(r, r.right)
    print CLOSEST_LEAF

    CLOSEST_LEAF = None
    CLOSEST_LEAF_DIST = maxint

    closest_leaf(r, r.right.left)
    print CLOSEST_LEAF

    CLOSEST_LEAF = None
    CLOSEST_LEAF_DIST = maxint

    closest_leaf(r, r.left)
    print CLOSEST_LEAF
