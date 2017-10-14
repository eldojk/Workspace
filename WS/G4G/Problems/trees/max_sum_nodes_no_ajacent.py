"""
amzn

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
