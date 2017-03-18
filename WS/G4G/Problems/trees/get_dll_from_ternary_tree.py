"""
http://www.geeksforgeeks.org/create-doubly-linked-list-ternary-ree/
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.mid = None

    def __repr__(self):
        return str(self.data)


def get_dll(root):
    if root.left:
        ls, le = get_dll(root.left)
    if root.mid:
        ms, me = get_dll(root.mid)
    if root.right:
        rs, re = get_dll(root.right)

    head = root
    if root.left:
        head.right = ls
        ls.left = head
        head = le
    if root.mid:
        head.right = ms
        ms.left = head
        head = me
    if root.right:
        head.right = rs
        rs.left = head
        head = re

    return root, head


if __name__ == '__main__':
    r = Node(3)

    r.left = Node(5)
    r.mid = Node(11)
    r.right = Node(63)

    r.left.left = Node(1)
    r.left.mid = Node(4)
    r.left.right = Node(8)
    r.mid.left = Node(6)
    r.mid.mid = Node(7)
    r.mid.right = Node(15)
    r.right.left = Node(31)
    r.right.mid = Node(55)
    r.right.right = Node(65)

    head, tail = get_dll(r)

    while head is not None:
        print head, '-',
        head = head.right
