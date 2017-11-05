"""
amzn

http://www.geeksforgeeks.org/merge-k-sorted-linked-lists/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll
from G4G.Problems.linked_list.merge_sorted_ll import sorted_merge


def merge_k_lists(linked_lists, last):

    while last != 0:
        i = 0
        j = last

        while i < j:

            # check this recursive sorted merge function
            linked_lists[i] = sorted_merge(linked_lists[i], linked_lists[j])

            i += 1
            j -= 1

            if i >= j:
                last = j

    return linked_lists[0]


if __name__ == '__main__':
    a = create_linked_list([1, 3, 5])
    b = create_linked_list([2, 4, 6, 8])
    c = create_linked_list([0, 9, 10, 11])

    res = merge_k_lists([a, b, c], 2)
    print_ll(res)
