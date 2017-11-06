"""
amzn

(more done down)
http://www.geeksforgeeks.org/maximum-sum-nodes-binary-tree-no-two-adjacent/
"""
from G4G.Problems.bst.vertical_sum import Node


def get_sum(root, hm):
    if root is None:
        return 0

    # reading from memo
    if hm.get(root) is not None:
        return hm[root]

    sum_excluding_root = get_sum(root.left, hm) + get_sum(root.right, hm)

    sum_including_root = root.data

    if root.left:
        sum_including_root += get_sum(root.left.left, hm) + get_sum(root.left.right, hm)

    if root.right:
        sum_including_root += get_sum(root.right.left, hm) + get_sum(root.right.right, hm)

    hm[root] = max(sum_excluding_root, sum_including_root)  # memoization to avoid recomputing

    return hm[root]


if __name__ == '__main__':
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(1)
    r.right.left = Node(4)
    r.right.right = Node(5)

    print get_sum(r, {})


"""
another approach
"""


def get_max_sum(root):
    if root is None:
        return 0, 0

    sum_incl_left, sum_excl_left = get_max_sum(root.left)
    sum_incl_right, sum_excl_right = get_max_sum(root.right)

    sum_incl = root.data + sum_excl_left + sum_excl_right

    sum_excl = max(sum_incl_left, sum_excl_left) + max(sum_incl_right, sum_excl_right)

    return sum_incl, sum_excl


if __name__ == '__main__':
    r = Node(1)
    r.left = Node(2)
    r.right = Node(3)
    r.left.left = Node(1)
    r.right.left = Node(4)
    r.right.right = Node(5)

    print get_max_sum(r)
