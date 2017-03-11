"""
http://www.geeksforgeeks.org/vertical-sum-in-a-given-binary-tree/
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def vsum(root, hd, dict):
    if root:
        vsum(root.left, hd - 1, dict)

        dict[hd] = root.data if dict.get(hd) is None else dict[hd] + root.data

        vsum(root.right, hd + 1, dict)


def vertical_sum(root):
    dict = {}
    vsum(root, 0, dict)

    print dict


def vprint(root, hd, dict):
    if root:
        dict[hd] = [root.data] if dict.get(hd) is None else dict[hd] + [root.data]

        vprint(root.left, hd - 1, dict)
        vprint(root.right, hd + 1, dict)


def vertical_print(root):
    dict = {}
    vprint(root, 0, dict)

    keys = dict.keys()
    keys.sort()

    for key in keys:
        print dict[key]


if __name__  == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    vertical_sum(root)
    print ''
    vertical_print(root)
