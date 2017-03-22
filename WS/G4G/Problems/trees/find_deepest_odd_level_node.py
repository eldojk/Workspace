"""
http://www.geeksforgeeks.org/depth-deepest-odd-level-node-binary-tree/
"""
from DS.algos.graphs.binary_tree import Node


def is_leaf(node):
    return node.left is None and node.right is None


def deepest_odd_level_node(root, level):
    if root is None:
        return None, level

    l_node, l_level = deepest_odd_level_node(root.left, level + 1)
    r_node, r_level = deepest_odd_level_node(root.right, level + 1)

    deepest_odd_level = level
    _deepest_odd_level_node = root

    if l_node is not None and l_level % 2 != 0:
        deepest_odd_level = l_level
        _deepest_odd_level_node = l_node

    if r_node is not None and r_level % 2 != 0 and deepest_odd_level < r_level:
        deepest_odd_level = r_level
        _deepest_odd_level_node = r_node

    return _deepest_odd_level_node, deepest_odd_level


if __name__ == '__main__':
    print ''
    r = Node(5)
    r.left = Node(10)
    r.right = Node(2)
    r.left.left = Node(3)
    r.left.right = Node(4)
    r.right.right = Node(15)
    r.left.right.left = Node(44)
    r.left.right.left.right = Node(12)
    r.right.right.left = Node(9)
    r.right.right.left = Node(8)

    print deepest_odd_level_node(r, 1)

    r = Node(10)
    r.left = Node(28)
    r.right = Node(13)
    r.right.left = Node(14)
    r.right.right = Node(15)
    r.right.right.left = Node(23)
    r.right.right.right = Node(24)

    print deepest_odd_level_node(r, 1)
