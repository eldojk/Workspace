"""
amzn

http://www.geeksforgeeks.org/find-the-largest-subtree-in-a-tree-that-is-also-a-bst/
"""
from sys import maxint
from G4G.Problems.bst.vertical_sum import Node

SIZE = 0


def largest_bst_size(root):
    global SIZE
    if root is None:
        # send is_bst, maximum node, minimum node and size of the largest bst
        return True, -maxint, maxint, 0

    is_left_bst, l_max, l_min, l_size = largest_bst_size(root.left)
    is_right_bst, r_max, r_min, r_size = largest_bst_size(root.right)

    if root.left is None:
        l_min = root.data

    if root.right is None:
        r_max = root.data

    if is_left_bst and is_right_bst and l_max < root.data < r_min:
        curr_size = l_size + r_size + 1

        if curr_size > SIZE:
            SIZE = curr_size

        return True, r_max, l_min, curr_size

    return False, r_max, l_min, l_size + r_size + 1


def get_largest_bst_size(root):
    global SIZE
    SIZE = 0
    largest_bst_size(root)
    return SIZE


if __name__ == '__main__':
    r = Node(5)
    r.left = Node(2)
    r.right = Node(4)
    r.left.left = Node(1)
    r.left.right = Node(3)

    print get_largest_bst_size(r)

    r = Node(50)
    r.left = Node(30)
    r.right = Node(60)
    r.left.left = Node(5)
    r.left.right = Node(20)
    r.right.left = Node(45)
    r.right.right = Node(70)
    r.right.right.left = Node(65)
    r.right.right.right = Node(80)

    print get_largest_bst_size(r)

    r = Node(60)
    r.left = Node(55)
    r.right = Node(70)
    r.left.left = Node(45)
    r.right.left = Node(65)
    r.right.right = Node(80)

    print get_largest_bst_size(r)
