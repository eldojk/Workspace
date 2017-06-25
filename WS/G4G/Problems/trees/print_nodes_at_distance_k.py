"""
amzn

http://www.geeksforgeeks.org/print-nodes-distance-k-given-node-binary-tree/
"""
from G4G.Problems.bst.vertical_sum import Node


def print_child_nodes_at_dist_k(root, k):
    if root is None:
        return

    if k == 0:
        print root

    print_child_nodes_at_dist_k(root.left, k - 1)
    print_child_nodes_at_dist_k(root.right, k - 1)


def print_at_dist_k(root, node, k):
    if root is None:
        return False, k

    if root == node:
        print_child_nodes_at_dist_k(root, k)
        return True, k

    is_found_left, l_dist = print_at_dist_k(root.left, node, k)
    if is_found_left:
        if l_dist == 1:
            print root
        elif l_dist > 1:
            print_child_nodes_at_dist_k(root.right, k - 2)

    is_found_right, r_dist = print_at_dist_k(root.right, node, k)
    if is_found_right:
        if r_dist == 1:
            print root
        elif r_dist > 1:
            print_child_nodes_at_dist_k(root.left, k - 2)

    return (is_found_left or is_found_right), k - 1


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
