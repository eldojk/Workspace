"""
http://www.geeksforgeeks.org/diameter-n-ary-tree/
"""


class Node(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def __repr__(self):
        return str(self.data)


def diameter(root):
    child_heights = []
    child_diameters = []

    for child in root.children:
        h, d = diameter(child)
        child_heights.append(h)
        child_diameters.append(d)

    # means no children, leaf node, so 1
    if len(child_heights) == 0:
        return 1, 1

    child_heights.sort()
    diameter_through_root = 1
    count = 0
    popped = []

    # getting top 2 child heights, because diameter through root should be from
    # 1 + top 2 root to leaf paths of max len (one for going up, reaching root and
    # going down by the other)
    while len(child_heights) > 0 and count < 2:
        popped.append(child_heights.pop())
        count += 1

    for el in popped:
        diameter_through_root += el

    # put them back since we need'em for later
    child_heights.extend(popped)

    height = 1 + max(child_heights)
    _diameter = max(child_diameters + [diameter_through_root])

    return height, _diameter


if __name__ == '__main__':
    r = Node(1)
    r.children = [Node(2) for i in range(3)]
    r.children[0].children = [Node(3) for i in range(3)]
    r.children[2].children = [Node(4), Node(4)]
    r.children[0].children[2].children = [Node(5), Node(5)]
    r.children[2].children[0].children = [Node(6)]
    r.children[0].children[2].children[0].children = [Node(7)]

    print diameter(r)
