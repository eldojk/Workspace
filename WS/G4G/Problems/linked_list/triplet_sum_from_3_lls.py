"""
amzn

#tricky
http://www.geeksforgeeks.org/find-a-triplet-from-three-linked-lists-with-sum-equal-to-a-given-number/
"""
from G4G.Problems.linked_list.linked_list import create_linked_list


def triplet_sum(sm, la, lb, lc):
    # sort lb in ascending and lc in descending order
    # for now assume they are sorted

    a = la
    while a is not None:
        b = lb
        c = lc

        while b is not None and c is not None:

            _sum = a.data + b.data + c.data
            if _sum == sm:
                print 'Found', a.data, b.data, c.data
                return True

            elif _sum < sm:
                b = b.nxt

            else:
                c = c.nxt

        a = a.nxt

    return False


if __name__ == '__main__':
    ha = create_linked_list([100, 15, 5, 20])
    hb = create_linked_list([2, 4, 9, 10])
    hc = create_linked_list([8, 4, 2, 1])

    triplet_sum(25, ha, hb, hc)
