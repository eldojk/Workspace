"""
http://www.geeksforgeeks.org/check-binary-tree-contains-duplicate-subtrees-size-2/
"""
from DS.algos.graphs.binary_tree import Node


def check_duplicate(root, hm):
    if root is None:
        return False, '$'

    is_found_left, ls = check_duplicate(root.left, hm)
    is_found_right, rs = check_duplicate(root.right, hm)

    s = root.data + ls + rs

    is_found = False

    # to consider non leaf nodes
    if len(s) > 3:
        if hm.get(s):
            is_found = True

        hm[s] = True

    return is_found_left or is_found_right or is_found, s


if __name__ == '__main__':
    r = Node('A')
    r.left = Node('B')
    r.right = Node('C')
    r.left.left = Node('D')
    r.left.right = Node('E')
    r.right.right = Node('B')
    r.right.right.left = Node('D')
    r.right.right.right = Node('E')

    print check_duplicate(r, {})

    # false case
    r = Node('A')
    r.left = Node('B')
    r.right = Node('C')
    r.left.left = Node('D')
    r.left.right = Node('E')
    r.right.right = Node('B')
    r.right.right.left = Node('D')
    r.right.right.right = Node('F')

    print check_duplicate(r, {})
