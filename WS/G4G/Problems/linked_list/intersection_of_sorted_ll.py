"""
amzn, msft

http://www.geeksforgeeks.org/intersection-of-two-sorted-linked-lists/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def add_to_result(rh, rt, node):
    if rt:
        rt.nxt = node
        return rh, rt.nxt

    rh = rt = node
    return rh, rt


def intersection_of_sorted_ll(h1, h2):
    rh = rt = None

    while h1 is not None and h2 is not None:

        if h1.data < h2.data:
            h1 = h1.nxt

        elif h1.data > h2.data:
            h2 = h2.nxt

        else:
            rh, rt = add_to_result(rh, rt, h1)
            h1 = h1.nxt
            h2 = h2.nxt

    rt.nxt = None
    return rh


if __name__ == '__main__':
    a = create_linked_list([1, 2, 2, 3, 4, 6])
    b = create_linked_list([2, 2, 4, 6, 8])
    res = intersection_of_sorted_ll(a, b)

    print_ll(res)
