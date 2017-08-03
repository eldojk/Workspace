"""
amzn

http://www.geeksforgeeks.org/print-nodes-distance-k-given-node-binary-tree/
"""
from G4G.Problems.bst.vertical_sum import Node


def print_child_nodes_at_dist_k(root, k):
    if root is None or k < 0:
        return

    if k == 0:
        print root
        return

    print_child_nodes_at_dist_k(root.left, k - 1)
    print_child_nodes_at_dist_k(root.right, k - 1)


def print_at_dist_k(root, node, k):
    if root is None or node is None:
        return -1

    if root == node:
        print_child_nodes_at_dist_k(root, k)
        return 1

    left_dist = print_at_dist_k(root.left, node, k)
    right_dist = print_at_dist_k(root.right, node, k)

    if left_dist > 0:
        print_child_nodes_at_dist_k(root.right, k - (left_dist + 1))
        return left_dist + 1

    if right_dist > 0:
        print_child_nodes_at_dist_k(root.left, k - (right_dist + 1))
        return right_dist + 1

    return -1


if __name__ == '__main__':
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    r.right.left = Node(6)
    r.right.right = Node(7)
    r.left.right.right = Node(8)
    r.left.right.right.left = Node(9)

    print_at_dist_k(r, r.left, 3)
