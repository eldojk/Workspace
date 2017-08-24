"""
amzn

http://www.geeksforgeeks.org/find-zeroes-to-be-flipped-so-that-number-of-consecutive-1s-is-maximized/
"""


class SubArrayFinder(object):
    def __init__(self, array, m):
        self.array = array
        self.l = 0
        self.r = 0
        self.num_zeroes = 0
        self.m = m
        self.max_width = 0
        self.max_l = 0
        self.max_r = 0

    def update_max_width(self):
        if self.r - self.l + 1 > self.max_width:
            self.max_width = self.r - self.l + 1
            self.max_l = self.l
            self.max_r = self.r

    def shrink(self):
        while self.array[self.l] == 1:
            self.l += 1

        if self.array[self.l] == 0:
            self.l += 1
            self.num_zeroes -= 1

    def print_zeroes(self, l, r):
        for i in range(l, r + 1):
            if self.array[i] == 0:
                print i,

    def get_sub_array(self):
        for i in range(len(self.array)):
            self.r = i
            if self.array[i] == 0:
                self.num_zeroes += 1

            if self.num_zeroes > self.m:
                self.shrink()

            self.update_max_width()

        print self.max_l, self.max_r
        self.print_zeroes(self.max_l, self.max_r)


if __name__ == '__main__':
    s = SubArrayFinder([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], 2)
    s.get_sub_array()

    print ''
    print ''

    s = SubArrayFinder([1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 1], 1)
    s.get_sub_array()

    print ''
    print ''

    s = SubArrayFinder([1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 0], 2)
    s.get_sub_array()
