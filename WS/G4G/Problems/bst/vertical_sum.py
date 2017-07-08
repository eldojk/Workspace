"""
amzn

http://www.geeksforgeeks.org/vertical-sum-in-a-given-binary-tree/
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.data)


def v_sum(root, hd, dict):
    if root:
        v_sum(root.left, hd - 1, dict)

        dict[hd] = root.data if dict.get(hd) is None else dict[hd] + root.data

        v_sum(root.right, hd + 1, dict)


def vertical_sum(root):
    dict = {}
    v_sum(root, 0, dict)

    print dict


def v_print(root, hd, dict):
    if root:
        dict[hd] = [root.data] if dict.get(hd) is None else dict[hd] + [root.data]

        v_print(root.left, hd - 1, dict)
        v_print(root.right, hd + 1, dict)


def vertical_print(root):
    _dict = {}
    v_print(root, 0, _dict)

    dict_keys = _dict.keys()
    dict_keys.sort()

    for k in dict_keys:
        print _dict[k]


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


"""
amzn

http://www.geeksforgeeks.org/bottom-view-binary-tree/
"""


def bottom_view(root, hd, dict, level):
    if root:
        if dict.get(hd) is not None and dict[hd][1] <= level:
            dict[hd] = (root.data, level)
        elif dict.get(hd) is None:
            dict[hd] = (root.data, level)

        bottom_view(root.left, hd - 1, dict, level + 1)
        bottom_view(root.right, hd + 1, dict, level + 1)


def b_view(root):
    dict = {}
    bottom_view(root, 0, dict, 0)

    return dict


if __name__ == '__main__':
    print ''
    root = Node(20)
    root.left = Node(8)
    root.right = Node(22)
    root.left.left = Node(5)
    root.left.right = Node(3)
    root.right.right = Node(25)
    root.right.left = Node(4)
    root.left.right.left = Node(10)
    root.left.right.right = Node(14)

    dict = b_view(root)

    keys = dict.keys()
    keys.sort()
    for key in keys:
        print dict[key][0],
