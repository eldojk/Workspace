from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array, Node

"""
http://www.geeksforgeeks.org/convert-bst-to-a-binary-tree/

Given a Binary Search Tree (BST), convert it to a Binary Tree such that every key of the original BST is changed to key
plus sum of all greater keys in BST.

Input: Root of following BST
              5
            /   \
           2     13

Output: The given BST is converted to following Binary Tree
              18
            /   \
          20     13
"""

from sys import maxint

sm = 0


def convert(root):
    global sm

    if root.right:
        convert(root.right)

    root.data += sm
    sm = root.data

    if root.left:
        convert(root.left)

    return root


r = Node(5)
r.left = Node(2)
r.right = Node(13)
print get_inorder_array(r, [])
root = convert(r)
print get_inorder_array(root, [])

"""
http://www.geeksforgeeks.org/check-whether-bst-contains-dead-end-not/
"""


def is_dead_end(root, mini, maxi):
    if abs(maxi - mini) == 1:
        return True

    if root is None:
        return False

    left_end = is_dead_end(root.left, mini, root.data)
    right_end = is_dead_end(root.right, root.data, maxi)

    if left_end and right_end:
        print root.data

    return left_end and right_end


r = Node(8)
r.left = Node(5)
r.right = Node(9)
r.left.left = Node(2)
r.left.right = Node(7)
r.left.left.left = Node(1)

is_dead_end(r, 0, maxint)

"""
http://www.geeksforgeeks.org/check-if-given-sorted-sub-sequence-exists-in-binary-search-tree/
"""

current_index = 0


def check_subsequence(root, array):
    global current_index
    if root.left:
        check_subsequence(root.left, array)

    if current_index < len(array) and root.data == array[current_index]:
        current_index += 1

    if root.right:
        check_subsequence(root.right, array)


root = Node(8)
root.left = Node(3)
root.right = Node(10)
root.left.left = Node(1)
root.left.right = Node(6)
root.right.right = Node(14)
root.left.right.left = Node(4)
root.left.right.right = Node(7)
root.right.right.left = Node(13)

array = [4, 6, 8, 14]
check_subsequence(root, array)
print current_index == len(array)

current_index = False
array = [1, 2, 3, 8]
check_subsequence(root, array)
print current_index == len(array)


"""
http://www.geeksforgeeks.org/in-place-convert-bst-into-a-min-heap/

Check sol. -> this one cobnverts bst to sorted ll
"""


def convert_to_sorted_linked_list(root, head):
    if root is None:
        return head

    head = convert_to_sorted_linked_list(root.right, head)

    root.right = head

    if head is not None:
        head.left = None

    head = root

    head = convert_to_sorted_linked_list(root.left, head)

    return head


root = Node(5)
root.left = Node(3)
root.right = Node(7)
root.left.left = Node(1)
root.left.right = Node(4)
root.right.right = Node(8)

h = convert_to_sorted_linked_list(root, None)
while h is not None:
    print h,
    h = h.right
