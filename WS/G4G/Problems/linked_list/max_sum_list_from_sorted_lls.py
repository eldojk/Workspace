"""
amzn

http://www.geeksforgeeks.org/maximum-sum-linked-list-two-sorted-linked-lists-common-nodes/
"""
from G4G.Problems.linked_list.linked_list import print_ll, create_linked_list


def get_max_list(a, b):
    result = None
    pre1 = curr1 = a
    pre2 = curr2 = b

    while curr1 is not None or curr2 is not None:
        sum1 = 0
        sum2 = 0

        # iterating till and equal node is found
        while curr1 is not None and curr2 is not None and curr1.data != curr2.data:

            if curr1.data < curr2.data:
                sum1 += curr1.data
                curr1 = curr1.nxt
            else:
                sum2 += curr2.data
                curr2 = curr2.nxt

        # if one of them becomes none in the process
        if curr1 is None:
            while curr2 is not None:
                sum2 += curr2.data
                curr2 = curr2.nxt

        if curr2 is None:
            while curr1 is not None:
                sum1 += curr1.data
                curr1 = curr1.nxt

        # initialization of result for the first time based on sum
        if pre1 == a and pre2 == b:
            result = pre1 if sum1 > sum2 else pre2

        else:
            # further decisions based on sum
            if sum1 > sum2:
                pre2.nxt = pre1.nxt
            else:
                pre1.nxt = pre2.nxt

        pre1 = curr1
        pre2 = curr2

        if curr1 is not None:
            curr1 = curr1.nxt

        if curr2 is not None:
            curr2 = curr2.nxt

    if result:
        print_ll(result)


if __name__ == '__main__':
    _a = create_linked_list([1, 3, 30, 90, 120, 240, 511])
    _b = create_linked_list([0, 3, 12, 32, 90, 125, 240, 249])
    get_max_list(_a, _b)