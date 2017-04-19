"""
amzn

http://www.geeksforgeeks.org/merging-intervals/
"""
from G4G.Problems.stacks.stack import Stack


class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __lt__(self, other):
        return self.start < other.start

    def __gt__(self, other):
        return self.start > other.start

    def __eq__(self, other):
        return self.start == other.start


def is_overlapping(a, b):
    if a.end > b.start:
        return True

    return False


def merge(a, b):
    st = a.start
    en = a.end if a.end > b.end else b.end
    return Interval(st, en)


def merge_overlapping_intervals(array):
    # sort based on start time
    array.sort()
    s = Stack()
    s.push(array[0])

    for i in range(1, len(array)):
        if not s.is_empty():
            element = s.pop()
            curr_element = array[i]
            if is_overlapping(element, curr_element):
                s.push(merge(element, curr_element))
            else:
                s.push(element)
                s.push(curr_element)

    print [(i.start, i.end) for i in s.items]


print merge_overlapping_intervals([Interval(2, 4), Interval(5, 7), Interval(1, 3), Interval(6, 8)])