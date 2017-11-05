"""
http://www.geeksforgeeks.org/find-maximum-difference-between-nearest-left-and-right-smaller-elements/

Input : arr[] = {2, 1, 8}
Output : 1
Left smaller  LS[] {0, 0, 1}
Right smaller RS[] {1, 0, 0}
Maximum Diff of abs(LS[i] - RS[i]) = 1

Input  : arr[] = {2, 4, 8, 7, 7, 9, 3}
Output : 4
Left smaller   LS[] = {0, 2, 4, 4, 4, 7, 2}
Right smaller  RS[] = {0, 3, 7, 3, 3, 3, 0}
Maximum Diff of abs(LS[i] - RS[i]) = 7 - 3 = 4

Input : arr[] = {5, 1, 9, 2, 5, 1, 7}
Output : 1
"""

from G4G.Problems.stack.stack import Stack


def compute_left_smaller_diffs(array):
    s = Stack()
    diff_array = [None for i in array]

    for i in range(len(array)):
        element = array[i]
        while not s.is_empty() and s.peek() > element:
            s.pop()

        if s.is_empty():
            diff_array[i] = 0
        else:
            diff_array[i] = s.peek()

        s.push(element)

    return diff_array


def compute_abs_diff(array):
    left_smaller = compute_left_smaller_diffs(array)

    reversed_array = array[::-1]
    right_smaller = compute_left_smaller_diffs(reversed_array)
    right_smaller = right_smaller[::-1]

    diff_array = []
    for i in range(len(array)):
        diff_array.append(abs(left_smaller[i] - right_smaller[i]))

    return max(diff_array)


print compute_abs_diff([2, 1, 8])
print compute_abs_diff([2, 4, 8, 7, 7, 9, 3])
print compute_abs_diff([5, 1, 9, 2, 5, 1, 7])
