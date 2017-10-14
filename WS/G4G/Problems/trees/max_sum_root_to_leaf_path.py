"""
Find the maximum sum leaf to root path in a Binary Tree
Given a Binary Tree, find the maximum sum path from a leaf to root.
For example, in the following tree, there are three
leaf to root paths 8->-2->10, -4->-2->10 and 7->10. The sums of these
three paths are 16, 4 and 17 respectively.
The maximum of them is 17 and the path for maximum is 7->10.

          10
       /      \
    -2        7
   /   \
8      -4

http://www.geeksforgeeks.org/find-the-maximum-sum-path-in-a-binary-tree/
"""
from G4G.Problems.bst.vertical_sum import Node


def max_sum_path(root, curr_sum):
    if root is None:
        return curr_sum

    l_sum = max_sum_path(root.left, curr_sum + root.data)
    r_sum = max_sum_path(root.right, curr_sum + root.data)
    return max(l_sum, r_sum)


if __name__ == '__main__':
    r = Node(10)
    r.left = Node(-2)
    r.right = Node(7)
    r.left.left = Node(12)
    r.left.right = Node(-4)

    print max_sum_path(r, 0)
