"""
amzn

http://www.geeksforgeeks.org/intersection-of-two-sorted-linked-lists/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def delete_ll_node(head):
    if head is None:
        return None

    nxt = head.nxt
    head.nxt = None
    return nxt


def intersection_of_sorted_ll(h1, h2):
    result = None
    p1 = p2 = None

    while h1 is not None and h2 is not None:
        if h1.data < h2.data:
            if p1:
                p1.nxt = delete_ll_node(h1)
                h1 = p1.nxt
            else:
                h1 = delete_ll_node(h1)

        elif h2.data < h1.data:
            if p2:
                p2.nxt = delete_ll_node(h2)
                h2 = p2.nxt
            else:
                h2 = delete_ll_node(h2)

        else:
            if result is None:
                result = h1

            p1 = h1
            p2 = h2
            h1 = h1.nxt
            h2 = h2.nxt

    return result


if __name__ == '__main__':
    a = create_linked_list([1, 2, 3, 4, 6])
    b = create_linked_list([2, 4, 6, 8])
    res = intersection_of_sorted_ll(a, b)

    print_ll(res)