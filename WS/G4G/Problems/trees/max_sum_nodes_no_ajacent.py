"""
amzn

(more done down)
http://www.geeksforgeeks.org/maximum-sum-nodes-binary-tree-no-two-adjacent/
"""
from G4G.Problems.bst.vertical_sum import Node


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
