"""
merge two sorted linked lists
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


def sorted_merge(a, b):
    if a is None:
        return b

    if b is None:
        return a

    if a.data > b.data:
        result = b
        result.nxt = sorted_merge(a, b.nxt)

    else:
        result = a
        result.nxt = sorted_merge(b, a.nxt)

    return result


if __name__ == '__main__':
    l1 = create_linked_list([1, 3, 5, 7, 9])
    l2 = create_linked_list([2, 4, 6, 8, 10])

    r = sorted_merge(l1, l2)
    print_ll(r)