"""
http://www.geeksforgeeks.org/in-place-convert-a-given-binary-tree-to-doubly-linked-list/
"""
from G4G.Problems.bst.vertical_sum import Node


def get_ll_head(node):
    while node.left:
        node = node.left

    return node


def get_ll_tail(node):
    while node.right:
        node = node.right

    return node


def binary_tree_to_dll(root, head):
    """
    converts to dll

    :param root:
    :param head: pointer to return? head or tail (boolean)
    :return:
    """
    if root is None:
        return None

    if root.left:
        left_tail = binary_tree_to_dll(root.left, False)
        left_tail.right = root
        root.left = left_tail

    if root.right:
        right_head = binary_tree_to_dll(root.right, True)
        right_head.left = root
        root.right = right_head

    if head:
        return get_ll_head(root)

    return get_ll_tail(root)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(12)
    root.right = Node(15)
    root.left.left = Node(25)
    root.left.right = Node(30)
    root.right.left = Node(36)

    ll_head = binary_tree_to_dll(root, True)

    iterator = ll_head
    while iterator:
        print iterator,
        iterator = iterator.right
