"""
http://www.geeksforgeeks.org/sort-elements-by-frequency/
"""


class Element(object):
    def __init__(self, val, freq, oc):
        self.val = val
        self.freq = freq
        self.oc = oc

    def __lt__(self, other):
        if self.freq != other.freq:
            return self.freq > other.freq

        return self.oc < other.oc

    def __gt__(self, other):
        if self.freq != other.freq:
            return self.freq < other.freq

        return self.oc > other.oc

    def __eq__(self, other):
        return self.val == other.val


def sort_by_freq(array):
    count = {}  # count
    oc = {}  # occurrence

    for i in range(len(array)):
        count[array[i]] = 1 if count.get(array[i]) is None else count[array[i]] + 1
        if oc.get(array[i]) is None:
            oc[array[i]] = i

    elements = []
    for key in count.keys():
        elements.append(Element(key, count[key], oc[key]))

    elements.sort()

    i = 0
    for el in elements:
        f = el.freq
        while f > 0:
            array[i] = el.val
            i += 1
            f -= 1

    return array


if __name__ == '__main__':
    print sort_by_freq([2, 5, 2, 8, 5, 6, 8, 8])
    print sort_by_freq([2, 5, 2, 6, -1, 9999999, 5, 8, 8, 8])