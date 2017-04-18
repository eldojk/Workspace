"""
http://qa.geeksforgeeks.org/3976/flattening-a-binary-tree
"""
from DS.algos.graphs.binary_tree import Node


def flatten(root):
    if root is None:
        return None

    # process right subtree
    right_head = flatten(root.right)

    if right_head:
        root.right = right_head

    left_head = flatten(root.left)

    # process left subtree, get left tail and attach root
    # to the tail
    if left_head:
        left_tail = left_head
        while left_tail.right is not None:
            left_tail = left_tail.right

        left_tail.right = root
        return left_head

    return root


def flatten2(root):
    if root is None:
        return None, None

    # process right subtree
    right_head, right_tail = flatten2(root.right)

    if right_head:
        root.right = right_head
    else:
        right_tail = root  # nothing in the right means no tail, hence root is the last node

    left_head, left_tail = flatten2(root.left)

    # process left subtree, get left tail and attach root
    # to the tail
    if left_head:
        left_tail.right = root
    else:
        left_head = root  # nothing in the left means no previous node, hence root is the first node

    return left_head, right_tail


if __name__ == '__main__':
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    r.right.left = Node(6)
    r.right.right = Node(7)

    h, t = flatten(r)

    while h is not None:
        print h,
        h = h.right


if __name__ == '__main__':
    print ''
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(4)
    r.left.right = Node(5)
    r.right.left = Node(6)
    r.right.right = Node(7)

    h, t = flatten2(r)

    while h is not None:
        print h,
        h = h.right
