"""
amzn

http://www.geeksforgeeks.org/sort-linked-list-already-sorted-absolute-values/

An important observation is, all negative elements are present in reverse order.
So we traverse the list, whenever we find an element that is out of order,
we move it to the front of linked list.

Input : 1 -> -2 -> -3 -> 4 -> -5
output: -5 -> -3 -> -2 -> 1 -> 4
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def sort_abs_val_sorted_ll(head):
    curr = head.nxt
    prev = head

    while curr is not None:

        if curr.data < prev.data:

            prev.nxt = curr.nxt

            curr.nxt = head
            head = curr

            curr = prev

        else:
            prev = curr

        curr = curr.nxt

    return head


if __name__ == '__main__':
    h = create_linked_list([0, 1, -2, 3, 4, 5, -5])
    sh = sort_abs_val_sorted_ll(h)

    print_ll(sh)
