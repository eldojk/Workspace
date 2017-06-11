"""
http://www.geeksforgeeks.org/point-arbit-pointer-greatest-value-right-side-node-linked-list/
"""
from G4G.Problems.linked_list.recursive_reverse import reverse2


def greatest_on_right(head):
    # reverse and solve
    rev = reverse2(head)

    rh = rev
    grtst = rev

    while rev is not None:
        rev.arbit = grtst

        if rev.data > grtst.data:
            rev = grtst

    return reverse2(rh)

