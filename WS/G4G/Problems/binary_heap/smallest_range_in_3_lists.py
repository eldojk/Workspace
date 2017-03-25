"""
http://www.geeksforgeeks.org/find-smallest-range-containing-elements-from-k-lists/
"""
from DS.algos.binary_heap.priority_queue import MIN_PQ, PriorityQueue
from sys import maxint


class Element(object):
    def __init__(self, data, idx, array):
        self.data = data
        self.index = idx
        self.array = array

    def __lt__(self, other):
        return self.data < other.data

    def __gt__(self, other):
        return self.data > other.data

    def __eq__(self, other):
        return self.data == other.data

    def __repr__(self):
        return str(self.data)


def compute_range(array, N):
    k = len(array)

    minpq = PriorityQueue(k, MIN_PQ)

    _min = maxint
    _max = -maxint
    for i in range(k):
        el = Element(array[i][0], 0, i)
        minpq.insert(el)

        if el.data < _min:
            _min = el.data

        if el.data > _max:
            _max = el.data

    start = _min
    end = _max
    rang = _max - _min

    while True:
        min_el = minpq.delete_top()
        _min = min_el.data

        new_range = _max - _min

        if new_range < rang:
            rang = new_range
            start = _min
            end = _max

        nxt_array = min_el.array
        nxt_idx = min_el.index + 1

        if nxt_idx < N:
            nxt_el = Element(array[nxt_array][nxt_idx], nxt_idx, nxt_array)

            if nxt_el.data > _max:
                _max = nxt_el.data

        else:
            break

        minpq.insert(nxt_el)

    return start, end


if __name__ == '__main__':
    print compute_range([[4, 7, 9, 12, 15], [0, 8, 10, 14, 20], [6, 12, 16, 30, 50]], 5)
