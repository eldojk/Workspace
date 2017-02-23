"""
http://www.geeksforgeeks.org/populate-inorder-successor-for-all-nodes/
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.nxt = None

    def __repr__(self):
        return str(self.data)


NEXT = None


def populate_in_order_successor(root):
    global NEXT
    if root:
        populate_in_order_successor(root.right)

        root.nxt = NEXT
        NEXT = root

        populate_in_order_successor(root.left)


if __name__ == '__main__':
    root = Node(10)
    root.left = Node(8)
    root.right = Node(12)
    root.left.left = Node(3)

    populate_in_order_successor(root)
    print root.left.left.nxt, root.left.nxt, root.nxt, root.right.nxt
