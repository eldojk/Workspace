"""
amzn

this is less confusing the geeks4geeks implementation

http://www.geeksforgeeks.org/find-maximum-path-sum-in-a-binary-tree/

https://leetcode.com/problems/binary-tree-maximum-path-sum/#/solutions
"""
from G4G.Problems.bst.vertical_sum import Node
from sys import maxint


MAX_VAL = -maxint


def max_sum_path(root):
    global MAX_VAL
    if root is None:
        return 0

    l_sum = max(0, max_sum_path(root.left))
    r_sum = max(0, max_sum_path(root.right))

    # update max seen so far, l_sum = 0 means l_sum not considered
    MAX_VAL = max(MAX_VAL, l_sum + r_sum + root.data)

    # for parent use only one path. i.e. biggest path
    return max(l_sum, r_sum) + root.data


if __name__ == '__main__':
    r = Node(10)
    r.left = Node(2)
    r.right = Node(10)
    r.left.left = Node(20)
    r.left.right = Node(1)
    r.right.right = Node(-25)
    r.right.right.left = Node(3)
    r.right.right.right = Node(4)

    max_sum_path(r)
    print MAX_VAL
