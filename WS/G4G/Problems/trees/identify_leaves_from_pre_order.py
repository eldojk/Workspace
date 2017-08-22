"""
amzn

https://stackoverflow.com/questions/42407162/how-to-identify-the-leaf-nodes-of-a-binary-search-tree

[5,3,2,4,8,7,9]
"""
from sys import maxint

PRE_INDEX = 0


def id_leaves(pre_order, _min, _max):
    global PRE_INDEX

    if PRE_INDEX >= len(pre_order):
        return 0

    root = pre_order[PRE_INDEX]

    if not (_min < root < _max):
        return 0

    PRE_INDEX += 1

    count = 1
    l_count = id_leaves(pre_order, _min, root)
    r_count = id_leaves(pre_order, root, _max)

    if l_count == 0 and r_count == 0:
        print root,

    return count + l_count + r_count


if __name__ == '__main__':
    id_leaves([5, 3, 2, 4, 8, 7, 9], -maxint, maxint)
