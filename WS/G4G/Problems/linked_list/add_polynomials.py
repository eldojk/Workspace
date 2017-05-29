"""
amzn

http://www.geeksforgeeks.org/adding-two-polynomials-using-linked-list/
"""
from G4G.Problems.linked_list.linked_list import print_ll


class Node(object):
    def __init__(self, coeff, power):
        self.data = coeff
        self.power = power
        self.nxt = None

    def __repr__(self):
        return str(self.coeff)


def add_poly(l1, l2):
    lp = None
    sp = None

    if l1.power >= l2.power:
        lp = l1
        sp = l2

    else:
        lp = l2
        sp = l1

    res = lp

    while lp.power != sp.power:
        lp = lp.nxt

    while lp is not None:
        lp.data += sp.data
        lp = lp.nxt
        sp = sp.nxt

    return res


if __name__ == '__main__':
    l1 = Node(5, 2)
    l1.nxt = Node(4, 1)
    l1.nxt.nxt = Node(2, 0)

    l2 = Node(5, 1)
    l2.nxt = Node(5, 0)

    print_ll(add_poly(l1, l2))