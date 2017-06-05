"""
amzn

http://www.geeksforgeeks.org/in-place-conversion-of-sorted-dll-to-balanced-bst/
http://www.geeksforgeeks.org/sorted-linked-list-to-balanced-bst/


in place. we are creating bottom up way. check this
"""
from G4G.Problems.linked_list.linked_list import create_doubly_linked_list

HEAD = None


def convert(n):
    global HEAD
    if n <= 0:
        return None

    left = convert(n // 2)

    root = HEAD
    root.prev = left
    HEAD = HEAD.nxt

    right = convert(n - n // 2 - 1)
    root.nxt = right

    return root


if __name__ == '__main__':
    HEAD = create_doubly_linked_list([1, 2, 3, 4, 5, 6, 7])
    r = convert(7)
    print '   ', r
    print '', r.prev, '   ', r.nxt
    print r.prev.prev, '', r.prev.nxt, '', r.nxt.prev, '', r.nxt.nxt

