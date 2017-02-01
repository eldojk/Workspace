"""
http://www.geeksforgeeks.org/find-level-maximum-sum-binary-tree/

better one
"""
from G4G.Problems.bst.connect_nodes_at_a_level import Node


def custom_traversal(root, level, sums):
    if root is None:
        return

    sums[level] = root.data if sums.get(level) is None else sums[level] + root.data
    custom_traversal(root.left, level+1, sums)
    custom_traversal(root.right, level+1, sums)


def compute_max_level_sum(root):
    sums = {}

    custom_traversal(root, 0, sums)

    return max(sums.values())


r = Node(1)
r.left = Node(2)
r.right = Node(3)
r.left.left = Node(4)
r.left.right = Node(5)
r.right.right = Node(8)
r.right.right.left = Node(6)
r.right.right.right = Node(7)

print compute_max_level_sum(r)