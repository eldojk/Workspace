"""
http://www.geeksforgeeks.org/find-all-possible-trees-with-given-inorder-traversal/

Let given inorder traversal be in[]. In the given traversal, all nodes in left subtree of in[i] must appear before it
and in right subtree must appear after it. So when we consider in[i] as root, all elements from in[0] to in[i-1] will be
in left subtree and in[i+1] to n-1 will be in right subtree. If in[0] to in[i-1] can form x different trees and in[i+1]
to in[n-1] can from y different trees then we will have x*y total trees when in[i] as root.
So we simply iterate from 0 to n-1 for root. For every node in[i], recursively find different left and right subtrees.

1) Initialize list of Binary Trees as empty.
2) For every element in[i] where i varies from 0 to n-1,
    do following
......a)  Create a new node with key as 'arr[i]',
          let this node be 'node'
......b)  Recursively construct list of all left subtrees.
......c)  Recursively construct list of all right subtrees.
3) Iterate for all left subtrees
   a) For current leftsubtree, iterate for all right subtrees
        Add current left and right subtrees to 'node' and add
        'node' to list.
"""
from G4G.Problems.bst.vertical_sum import Node


def get_all_trees(arr, start, end):
    if start > end:
        return [None]

    trees = []

    for i in range(start, end + 1):
        l_trees = get_all_trees(arr, start, i - 1)

        r_trees = get_all_trees(arr, i + 1, end)

        for j in l_trees:
            for k in r_trees:

                node = Node(arr[i])

                node.left = j
                node.right = k

                trees.append(node)

    return trees


if __name__ == '__main__':
    t = get_all_trees([4, 5, 7], 0, 2)  # notice we are passing 0, 2 instead of 0,3. this handles all corner cases
    print t