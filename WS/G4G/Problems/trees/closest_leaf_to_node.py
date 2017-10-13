"""
amzn

http://www.geeksforgeeks.org/find-closest-leaf-binary-tree/
"""
from sys import maxint
from G4G.Problems.bst.vertical_sum import Node


def is_leaf(node):
    return node.left is None and node.right is None


def find_closest_leaf_dist(root):
    if is_leaf(root):
        return 0

    l_dist = maxint
    if root.left:
        l_dist = find_closest_leaf_dist(root.left)

    r_dist = maxint
    if root.right:
        r_dist = find_closest_leaf_dist(root.right)

    return 1 + min(l_dist, r_dist)


def find_closest(root, node):
    if root is None:
        return False, 0, 0

    if node == root.data:
        min_dist = find_closest_leaf_dist(root)
        return True, 1, min_dist

    left_found, left_node_dist, left_min_dist = find_closest(root.left, node)
    right_found, right_node_dist, right_min_dist = find_closest(root.right, node)

    if left_found:
        if root.right:
            min_dist = find_closest_leaf_dist(root.right)
            min_dist = min(
                min_dist + 1 + left_node_dist,
                left_min_dist
            )

            return True, left_node_dist + 1, min_dist

        return True, left_node_dist + 1, left_min_dist

    if right_found:
        if root.left:
            min_dist = find_closest_leaf_dist(root.left)
            min_dist = min(
                min_dist + 1 + right_node_dist,
                right_min_dist
            )

            return True, right_node_dist + 1, min_dist

        return True, right_node_dist + 1, right_min_dist

    return False, 0, 0


def get_dist_of_closest_leaf(root, node):
    is_found, ld, min_dist = find_closest(root, node)

    if is_found:
        return min_dist

    return None


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

    print get_dist_of_closest_leaf(r, 'H')
    print get_dist_of_closest_leaf(r, 'C')
    print get_dist_of_closest_leaf(r, 'E')
    print get_dist_of_closest_leaf(r, 'B')
