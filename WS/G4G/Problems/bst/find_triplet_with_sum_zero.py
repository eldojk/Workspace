"""
amzn : triplets adding to given val in array -> sort the array and do the same

http://www.geeksforgeeks.org/find-if-there-is-a-triplet-in-bst-that-adds-to-0/
http://www.geeksforgeeks.org/find-a-triplet-that-sum-to-a-given-value/
"""
from G4G.Problems.bst.merge_two_balanced_bst import get_inorder_array, Node


def get_doubles_with_sum(array, start, end, _sum):
    while start < end:
        if array[start] + array[end] == _sum:
            return start, end
        elif array[start] + array[end] < _sum:
            start += 1
        else:
            end -= 1

    return None, None


def triplets_adding_to_zero(array):
    for i in range(len(array) - 2):
        expected_doublet_sum = array[i] * -1
        start = i + 1
        end = len(array) - 1

        m, n = get_doubles_with_sum(array, start, end, expected_doublet_sum)

        if m is None:
            continue
        else:
            return array[i], array[m], array[n]

    return None, None, None


if __name__ == '__main__':
    r = Node(6)
    r.left = Node(-13)
    r.right = Node(14)
    r.left.right = Node(-8)
    r.right.left = Node(13)
    r.right.right = Node(15)
    r.right.left.left = Node(7)

    in_order = get_inorder_array(r, [])
    print triplets_adding_to_zero(in_order)
