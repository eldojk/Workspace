"""
amzn, msft

#tricky
http://www.geeksforgeeks.org/median-of-stream-of-integers-running-integers/
"""
from DS.algos.binary_heap.priority_queue import MAX_PQ, MIN_PQ, PriorityQueue


class RunningMedian(object):
    def __init__(self):
        self.ar = []
        self.med = None
        self.max_pq = PriorityQueue(100, MAX_PQ)
        self.max_pq_len = 0
        self.min_pq = PriorityQueue(100, MIN_PQ)
        self.min_pq_len = 0
        self.processed_first_two = False

    def balance(self):
        if abs(self.max_pq_len - self.min_pq_len) > 1:
            if self.max_pq_len > self.min_pq_len:
                self.min_pq.insert(self.max_pq.delete_top())
                self.min_pq_len += 1
                self.max_pq_len -= 1
            else:
                self.max_pq.insert(self.min_pq.delete_top())
                self.max_pq_len += 1
                self.min_pq_len -= 1

    def compute_median(self):
        if self.max_pq_len > self.min_pq_len:
            self.med = '%.2f' % self.max_pq.array[1]
        elif self.min_pq_len > self.max_pq_len:
            self.med = '%.2f' % self.min_pq.array[1]
        else:
            self.med = '%.2f' % ((self.min_pq.array[1] + self.max_pq.array[1]) / 2)

    def add(self, num):
        if len(self.ar) == 0:
            self.ar.append(num)
            self.med = '%.2f' % num

        elif len(self.ar) == 1:
            self.ar.append(num)
            self.med = '%.2f' % ((self.ar[0] + self.ar[1]) / 2)

        else:
            if not self.processed_first_two:
                less = 0 if self.ar[0] < self.ar[1] else 1
                grtr = 0 if less == 1 else 1
                self.max_pq.insert(self.ar[less])
                self.min_pq.insert(self.ar[grtr])
                self.max_pq_len += 1
                self.min_pq_len += 1
                self.processed_first_two = True

            if num <= self.max_pq.array[1]:
                self.max_pq.insert(num)
                self.max_pq_len += 1
            else:
                self.min_pq.insert(num)
                self.min_pq_len += 1

            self.balance()
            self.compute_median()

    def get_median(self):
        return self.med
