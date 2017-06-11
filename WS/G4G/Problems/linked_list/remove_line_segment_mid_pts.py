"""
msft

http://www.geeksforgeeks.org/given-linked-list-line-segments-remove-middle-points/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list, print_ll


class Node(object):
    def __init__(self, data):
        self.data = data
        self.nxt = None

    def __repr__(self):
        return str(self.data)

    def x(self):
        return self.data[0]

    def y(self):
        return self.data[1]


def remove_mid_points(head):
    hd = head
    while head is not None and \
                    head.nxt is not None and \
                    head.nxt.nxt is not None:

        a = head
        b = head.nxt
        c = head.nxt.nxt

        if a.x() == b.x() == c.x():
            a.nxt = c

        elif a.y() == b.y() == c.y():
            a.nxt = c

        else:
            head = head.nxt

    return hd


if __name__ == '__main__':
    h = create_linked_list([(0, 10), (1, 10), (5, 10), (7, 10), (7, 5), (20, 5), (40, 5)], node=Node)
    res = remove_mid_points(h)
    print_ll(res)

    print ''

    h = create_linked_list([(2, 3), (4, 3), (6, 3), (10, 3), (12, 3)], node=Node)
    res = remove_mid_points(h)
    print_ll(res)
