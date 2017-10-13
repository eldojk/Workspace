"""
amzn

http://www.geeksforgeeks.org/minimum-sum-squares-characters-counts-given-string-removing-k-characters/
"""
from DS.algos.binary_heap.priority_queue import MAX_PQ, PriorityQueue


class Node(object):
    def __init__(self, val, count):
        self.val = val
        self.count = count

    def __lt__(self, other):
        return self.count < other.count

    def __gt__(self, other):
        return self.count > other.count

    def __eq__(self, other):
        return self.count == other.count


def get_char_counts(string):
    hm = {}

    for c in string:
        if c in hm:
            hm[c] += 1

        else:
            hm[c] = 1

    keys = hm.keys()
    pq = PriorityQueue(len(keys), MAX_PQ)

    for k in keys:
        pq.insert(Node(k, hm[k]))

    return pq


def min_sum_square_char_counts(string, k):
    pq = get_char_counts(string)

    while k > 0:
        el = pq.delete_top()
        el.count -= 1

        if el.count != 0:
            pq.insert(el)

        k -= 1

    result = 0
    while not pq.is_empty():
        el = pq.delete_top()

        result += el.count ** 2

    return result


if __name__ == '__main__':
    print min_sum_square_char_counts('abccc', 1)
    print min_sum_square_char_counts('aaab', 2)
    print min_sum_square_char_counts('saideep', 1)
