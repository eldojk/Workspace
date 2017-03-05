"""
http://www.geeksforgeeks.org/remove-all-nodes-which-lie-on-a-path-having-sum-less-than-k/
"""
from G4G.Problems.bst.vertical_sum import Node
from G4G.Problems.trees.level_order_traversal import print_level_order


def is_leaf(node):
    return node.left is None and node.right is None


def remove_paths_without_min_sum(root, curr_sum, k):
    if root is None:
        return True

    curr_sum += root.data

    is_left_sum_satisfied = remove_paths_without_min_sum(root.left, curr_sum, k)
    is_right_sum_satisfied = remove_paths_without_min_sum(root.right, curr_sum, k)

    if not is_left_sum_satisfied:
        root.left = None

    if not is_right_sum_satisfied:
        root.right = None

    if is_leaf(root):
        return curr_sum >= k

    return is_right_sum_satisfied or is_right_sum_satisfied


def remove_nodes(root, k):
    remove_paths_without_min_sum(root, 0, k)
    return root


if __name__ == '__main__':
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.right = Node(4)
    root.left.right = Node(5)

    root.right.left = Node(6)
    root.right.right = Node(7)

    remove_nodes(root, 11)

    print_level_order(root)