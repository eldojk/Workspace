from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array, Node
from sys import maxint


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

Check sol. -> this one converts bst to sorted ll
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


if __name__ == '__main__':
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


"""
amzn

ceiling of bst
http://www.geeksforgeeks.org/floor-and-ceil-from-a-bst/
"""


def ceiling(root, _input):
    if root is None:
        return None

    if root.data == _input:
        return root.data

    if root.data < _input:
        return ceiling(root.right, _input)

    ceil = ceiling(root.left, _input)
    if ceil is not None and ceil >= _input:
        return ceil

    return root.data


if __name__ == '__main__':
    print ''
    root = Node(8)
    root.left = Node(4)
    root.right = Node(12)
    root.left.left = Node(2)
    root.left.right = Node(6)
    root.right.left = Node(10)
    root.right.right = Node(14)

    for i in range(16):
        print i, ceiling(root, i), ' || ',


def floor(root, _input):
    if root is None:
        return None

    if root.data == _input:
        return root.data

    if root.data > _input:
        return floor(root.left, _input)

    flr = floor(root.right)
    if flr is not None and flr <= _input:
        return flr

    return root.data
