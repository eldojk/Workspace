"""
amzn, msft

http://www.geeksforgeeks.org/lca-n-ary-tree-constant-query-o1/
"""


class NNode(object):
    def __init__(self, data):
        self.data = data
        self.children = []

    def __repr__(self):
        return str(self.data)


def euler_walk(root, array, depths, height):
    array.append(root.data)
    depths.append(height)

    for child in root.children:
        euler_walk(child, array, depths, height + 1)
        array.append(root.data)
        depths.append(height)


def find_indices(array, num1, num2):
    i1 = -1
    i2 = -1
    for i in range(len(array)):
        if array[i] == num1:
            i1 = i
        if array[i] == num2:
            i2 = i

    return i1, i2


def lca(root, n1, n2):
    euler = []
    depths = []
    euler_walk(root, euler, depths, 0)

    i1, i2 = find_indices(euler, n1, n2)

    if i1 == -1 or i2 == -1:
        print 'Cant find required element(s)'
        return

    if i1 == i2:
        # both are same
        print euler[i1]
        return

    if abs(i1 - i2) == 1:
        # one of them is the ancestor
        min_depth_i = i1 if depths[i1] < depths[i2] else i2
        print euler[min_depth_i]
        return

    # smallest depth value node between i1 and i2 will be the lca
    min_idx = i1 + 1
    for i in range(i1 + 1, i2):
        if euler[i] < euler[min_idx]:
            min_idx = i

    print euler[min_idx]


if __name__ == '__main__':
    r = NNode(1)
    r.children = [NNode(2), NNode(3)]
    r.children[0].children = [NNode(i) for i in range(4, 7)]
    r.children[1].children = [NNode(7), NNode(8)]

    lca(r, 6, 7)
    lca(r, 6, 4)