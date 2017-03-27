"""
http://www.geeksforgeeks.org/full-and-complete-binary-tree-from-given-preorder-and-postorder-traversals/

It is not possible to construct a general Binary Tree from preorder and postorder traversals (See this). But if know
that the Binary Tree is Full, we can construct the tree without ambiguity.

Let us consider the two given arrays as pre[] = {1, 2, 4, 8, 9, 5, 3, 6, 7} and post[] = {8, 9, 4, 5, 2, 6, 7, 3, 1};
In pre[], the leftmost element is root of tree. Since the tree is full and array size is more than 1. The value next to
1 in pre[], must be left child of root. So we know 1 is root and 2 is left child. How to find the all nodes in left
subtree? We know 2 is root of all nodes in left subtree. All nodes before 2 in post[] must be in left subtree. Now we
know 1 is root, elements {8, 9, 4, 5, 2} are in left subtree, and the elements {6, 7, 3} are in right subtree.


                  1
                /   \
               /      \
     {8, 9, 4, 5, 2}     {6, 7, 3}

We recursively follow the above approach and get the following tree.

          1
        /   \
      2       3
    /  \     /  \
   4    5   6    7
  / \
 8   9

"""
from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array
from G4G.Problems.bst.vertical_sum import Node
# todo Not sure of this

PRE_INDEX = 0


def search(array, element, start, end):
    for i in range(start, end):
        if array[i] == element:
            break

    return i


def construct_tree(pre, post, start, end, N):
    global PRE_INDEX

    if PRE_INDEX >= N or start > end:
        return None

    root = Node(pre[PRE_INDEX])
    PRE_INDEX += 1

    if start == end:
        return root

    index = search(post, pre[PRE_INDEX], start, end)

    if index <= end:
        root.left = construct_tree(pre, post, start, index, N)
        root.right = construct_tree(pre, post, index + 1, end, N)

    return root


if __name__ == '__main__':
    t = construct_tree([1, 2, 4, 8, 9, 5, 3, 6, 7], [8, 9, 4, 5, 2, 6, 7, 3, 1], 0, 8, 9)
    print get_inorder_array(t, [])