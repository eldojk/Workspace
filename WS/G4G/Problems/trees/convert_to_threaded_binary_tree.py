"""
http://www.geeksforgeeks.org/convert-binary-tree-threaded-binary-tree/
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.successor = None

    def __repr__(self):
        return str(self.data)


def convert(root):
    if root is None:
        return None

    pred = convert(root.left)

    if pred:
        pred.successor = root

    last_node = convert(root.right)

    if last_node:
        return last_node

    return root


def _in_order_print(root):
    if root:
        _in_order_print(root.left)

        if root.successor:
            print root, '->', root.successor
        else:
            print root, '->', root.right

        _in_order_print(root.right)


if __name__ == '__main__':
    r = Node(6)
    r.left = Node(3)
    r.right = Node(8)
    r.left.left = Node(1)
    r.left.right = Node(5)
    r.right.left = Node(7)
    r.right.right = Node(11)
    r.right.right.left = Node(9)
    r.right.right.right = Node(13)

    convert(r)
    _in_order_print(r)
