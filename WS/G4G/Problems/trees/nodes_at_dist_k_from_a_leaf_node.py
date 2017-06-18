"""
msft

http://www.geeksforgeeks.org/print-nodes-distance-k-leaf-node/
"""
from G4G.Problems.bst.vertical_sum import Node


def is_leaf(node):
    return node.left is None and node.right is None


def print_nodes_at_dist_k_from_a_leaf(root, k):
    if is_leaf(root):
        return [1]

    distances = []
    if root.left:
        left_distances = print_nodes_at_dist_k_from_a_leaf(root.left, k)
        distances += left_distances

    if root.right:
        right_distances = print_nodes_at_dist_k_from_a_leaf(root.right, k)
        distances += right_distances

    if any(d == k for d in distances):
        print root,

    return [d + 1 for d in distances]


if __name__ == '__main__':
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    r.right.left = Node(6)
    r.right.right = Node(7)
    r.right.left.right = Node(8)

    print_nodes_at_dist_k_from_a_leaf(r, 1)
    print ''
    print_nodes_at_dist_k_from_a_leaf(r, 2)
