"""
amzn, msft

http://www.geeksforgeeks.org/remove-bst-keys-outside-the-given-range/
"""
from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array, Node


def remove_nodes_out_of_range(root, rang):
    if root is None:
        return None

    root.left = remove_nodes_out_of_range(root.left, rang)
    root.right = remove_nodes_out_of_range(root.right, rang)

    if root.data < rang[0]:
        return root.right

    if root.data > rang[1]:
        return root.left

    return root


if __name__ == '__main__':
    r = Node(6)
    r.left = Node(-13)
    r.right = Node(14)
    r.left.right = Node(-8)
    r.right.left = Node(13)
    r.right.right = Node(15)
    r.right.left.left = Node(7)
    root = remove_nodes_out_of_range(r, (-10, 13))

    in_order = get_inorder_array(r, [])
    print in_order
