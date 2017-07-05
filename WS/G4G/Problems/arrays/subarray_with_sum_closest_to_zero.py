"""
msft

http://www.geeksforgeeks.org/find-sub-array-sum-closest-0/
"""
from sys import maxint


class Element(object):
    def __init__(self, sm, index):
        self.sum = sm
        self.index = index

    def __lt__(self, other):
        return self.sum < other.sum

    def __gt__(self, other):
        return self.sum > other.sum

    def __eq__(self, other):
        return self.sum == other.sum

    def __repr__(self):
        return str(self.sum)


def prefix_sum(array):
    sm = 0
    ps = []

    for i in range(len(array)):
        sm += array[i]
        ps.append(Element(sm, i))

    return ps


def sub_array_with_sum_closest_to_zero(array):
    pf = prefix_sum(array)
    pf.sort()

    a = -1
    b = -1
    min_diff = maxint

    if pf[0].sum == 0:  # if we find a zero sum, return it
        return 0, pf[0].index

    for i in range(1, len(pf)):
        if pf[i].sum == 0:  # if we find a zero sum, return it
            return 0, pf[i].index

        diff = pf[i].sum - pf[i - 1].sum

        if diff < min_diff:
            min_diff = diff
            a = pf[i - 1].index
            b = pf[i].index

    return (a + 1, b) if a < b else (b + 1, a)


if __name__ == '__main__':
    print sub_array_with_sum_closest_to_zero([2, 3, -4, -1, 6])
    print sub_array_with_sum_closest_to_zero([-1, 3, 2, -5, 4])
    print sub_array_with_sum_closest_to_zero([2, -5, 4, -6, 3])