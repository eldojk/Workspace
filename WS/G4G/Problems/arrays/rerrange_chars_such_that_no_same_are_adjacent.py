"""
amzn

http://www.zrzahid.com/rearrange-characters-in-string-with-no-adjacent-duplicate-characters/
"""
from DS.algos.binary_heap.priority_queue import PriorityQueue, MAX_PQ
from math import ceil


class CharFreq(object):
    def __init__(self, ch, fr):
        self.char = ch
        self.freq = fr

    def __lt__(self, other):
        return self.freq < other.freq

    def __gt__(self, other):
        return self.freq > other.freq

    def __eq__(self, other):
        return self.freq == other.freq


def re_arrange(string):
    li = list(string)
    n = len(li)
    cc = [0 for i in range(26)]

    for i in xrange(len(string)):
        c = string[i]
        idx = ord(c) - ord('a')
        cc[idx] += 1

        if cc[idx] > ceil(n / 2.0):
            print cc[idx]
            return 'Nope'

    pq_size = 0
    for i in range(len(cc)):
        if cc[i] != 0:
            pq_size += 1

    pq = PriorityQueue(pq_size, MAX_PQ)

    for i in xrange(26):
        if cc[i] != 0:
            pq.insert(CharFreq(chr(i + ord('a')), cc[i]))

    res = []
    while not pq.is_empty():
        first = pq.delete_top()
        res.append(first.char)
        first.freq -= 1

        second = None
        if not pq.is_empty():
            second = pq.delete_top()
            res.append(second.char)
            second.freq -= 1

        if first.freq > 0:
            pq.insert(first)

        if second is not None and second.freq > 0:
            pq.insert(second)

    return ''.join(res)


if __name__ == '__main__':
    print re_arrange('aaabc')