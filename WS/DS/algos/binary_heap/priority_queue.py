MAX_PQ = 0
MIN_PQ =1


class PriorityQueue(object):
    def __init__(self, size, type):
        self.array = [None for i in range(size + 1)]
        self.N = 0
        self.type = type

    def less(self, i, j):
        if j >= len(self.array) or self.array[j] is None:
            return False

        return self.array[i] < self.array[j] if self.type == MAX_PQ else self.array[i] > self.array[j]

    def exchange(self, i, j):
        temp = self.array[i]
        self.array[i] = self.array[j]
        self.array[j] = temp

    def swim(self, k):
        while k > 1:
            parent = int(k/2)
            if self.less(parent, k):
                self.exchange(parent, k)

            k = parent

    def sink(self, k):
        while 2*k <= self.N:
            child = 2*k
            if self.less(child, child+1):
                child += 1

            if not self.less(k, child):
                break

            self.exchange(k, child)
            k = child

    def is_empty(self):
        return self.N == 0

    def get_size(self):
        return self.N

    def get_top(self):
        return self.array[1]

    def insert(self, item):
        self.N += 1
        self.array[self.N] = item
        self.swim(self.N)

    def delete_top(self):
        top = self.array[1]
        self.exchange(1, self.N)
        self.N -= 1
        self.array[self.N + 1] = None
        self.sink(1)
        return top

