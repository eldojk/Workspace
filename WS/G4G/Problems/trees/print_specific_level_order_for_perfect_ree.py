"""
http://www.geeksforgeeks.org/perfect-binary-tree-specific-level-order-traversal/
"""
from Queue import Queue


class Node:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None


def print_specific_level_order(root):
    if root is None:
        return

    print root.data,

    if root.left is not None:
        print root.left.data,
        print root.right.data,

    if root.left.left is None:
        return

    q = Queue()
    q.put(root.left)
    q.put(root.right)

    while not q.empty():
        first = q.get()
        second = q.get()

        print first.left.data,
        print second.right.data,
        print first.right.data,
        print second.left.data,

        if first.left.left is not None:
            q.put(first.left)
            q.put(second.right)
            q.put(first.right)
            q.put(second.left)


if __name__ == '__main__':
    root = Node(1)

    root.left = Node(2)
    root.right = Node(3)

    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    root.left.left.left = Node(8)
    root.left.left.right = Node(9)
    root.left.right.left = Node(10)
    root.left.right.right = Node(11)
    root.right.left.left = Node(12)
    root.right.left.right = Node(13)
    root.right.right.left = Node(14)
    root.right.right.right = Node(15)

    root.left.left.left.left = Node(16)
    root.left.left.left.right = Node(17)
    root.left.left.right.left = Node(18)
    root.left.left.right.right = Node(19)
    root.left.right.left.left = Node(20)
    root.left.right.left.right = Node(21)
    root.left.right.right.left = Node(22)
    root.left.right.right.right = Node(23)
    root.right.left.left.left = Node(24)
    root.right.left.left.right = Node(25)
    root.right.left.right.left = Node(26)
    root.right.left.right.right = Node(27)
    root.right.right.left.left = Node(28)
    root.right.right.left.right = Node(29)
    root.right.right.right.left = Node(30)
    root.right.right.right.right = Node(31)

    print_specific_level_order(root)
