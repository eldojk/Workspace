"""
amzn, msft

http://www.geeksforgeeks.org/merge-sort-for-linked-list/

sorting using arbit ptr instead of nxt ptr will solve this
http://www.geeksforgeeks.org/point-to-next-higher-value-node-in-a-linked-list-with-an-arbitrary-pointer/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll
from G4G.Problems.linked_list.merge_sorted_ll import sorted_merge


def split(head):
    front = head

    if head is None or head.nxt is None:
        back = None

    else:
        f = head.nxt
        s = head

        while f is not None:
            f = f.nxt

            if f is not None:
                s = s.nxt
                f = f.nxt

        front = head
        back = s.nxt
        s.nxt = None

    return front, back


def merge_sort_ll(head):
    if head is None or head.nxt is None:
        return head

    a, b = split(head)

    a_result = merge_sort_ll(a)
    b_result = merge_sort_ll(b)

    head = sorted_merge(a_result, b_result)
    return head


if __name__ == '__main__':
    h = create_linked_list([4, 5, 3, 1, 0, 6, 2])
    h = merge_sort_ll(h)
    print_ll(h)
