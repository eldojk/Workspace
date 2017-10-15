# coding=utf-8
"""
amzn

Construct a special tree from given preorder traversal
Given an array ‘pre[]’ that represents Preorder traversal of a spacial
binary tree where every node has either 0 or 2 children. One more array
‘preLN[]’ is given which has only two possible values ‘L’ and ‘N’. The
value ‘L’ in ‘preLN[]’ indicates that the corresponding node in Binary
Tree is a leaf node and value ‘N’ indicates that the corresponding node
is non-leaf node. Write a function to construct the tree from the given
two arrays.

Example:

Input:  pre[] = {10, 30, 20, 5, 15},  preLN[] = {'N', 'N', 'L', 'L', 'L'}
Output: Root of following tree
          10
         /  \
        30   15
       /  \
      20   5

http://www.geeksforgeeks.org/construct-a-special-tree-from-given-preorder-traversal/
"""
from G4G.Problems.bst.vertical_sum import Node

index = 0


def create_tree(pre, pre_ln):
    global index

    if index >= len(pre):
        return None

    root = Node(pre[index])

    if pre_ln[index] == 'L':
        index += 1
        return root

    index += 1
    root.left = create_tree(pre, pre_ln)
    root.right = create_tree(pre, pre_ln)

    return root


if __name__ == '__main__':
    rt = create_tree([10, 30, 20, 5, 15], ['N', 'N', 'L', 'L', 'L'])

    print rt
    print rt.left
    print rt.right
    print rt.left.left
    print rt.left.right
