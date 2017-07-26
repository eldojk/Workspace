"""
amzn

http://www.geeksforgeeks.org/print-cousins-of-a-given-node-in-binary-tree/
"""
from G4G.Problems.trees.tree_problems2 import get_std_tree


def get_sibling_and_level(root, key, level):
    if root is None:
        return None

    if root.left is not None and root.left.data == key:
        return root.right, level + 1

    elif root.right is not None and root.right.data == key:
        return root.left, level + 1

    l_res = get_sibling_and_level(root.left, key, level + 1)
    r_res = get_sibling_and_level(root.right, key, level + 1)

    return l_res if l_res is not None else r_res


def print_cousins(root, level, node, sibling, target_level):
    if root is None:
        return

    if level == target_level and root.data != node and root.data != sibling:
        print root

    print_cousins(root.left, level + 1, node, sibling, target_level)
    print_cousins(root.right, level + 1, node, sibling, target_level)


if __name__ == '__main__':
    r = get_std_tree()
    sib, lvl = get_sibling_and_level(r, 4, 0)
    print_cousins(r, 0, 4, sib.data, lvl)