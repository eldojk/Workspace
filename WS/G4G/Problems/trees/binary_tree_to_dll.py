"""
amzn, msft

see other imps down

http://www.geeksforgeeks.org/in-place-convert-a-given-binary-tree-to-doubly-linked-list/
"""
from G4G.Problems.bst.vertical_sum import Node


def bt_to_dll(root):
    if root is None:
        return None, None

    left_head, left_tail = bt_to_dll(root.left)
    right_head, right_tail = bt_to_dll(root.right)

    head = tail = root

    if left_tail:
        left_tail.right = root
        root.left = left_tail
        head = left_head

    if right_head:
        root.right = right_head
        right_head.left = root
        tail = right_tail

    return head, tail


if __name__ == '__main__':
    r = Node(10)
    r.left = Node(12)
    r.right = Node(15)
    r.left.left = Node(25)
    r.left.right = Node(30)
    r.right.left = Node(36)

    ll_head, ll_tail = bt_to_dll(r)

    iterator = ll_head
    while iterator:
        print iterator,
        iterator = iterator.right


"""
http://www.geeksforgeeks.org/convert-a-binary-tree-to-a-circular-doubly-link-list/

To do this, just connect head and tail from the above
"""
