"""
http://www.geeksforgeeks.org/kth-largest-element-in-a-stream/
"""
from DS.algos.binary_heap.priority_queue import PriorityQueue, MIN_PQ


class KthLargest(object):
    def __init__(self, k):
        self.k = k
        self.min_pq = PriorityQueue(k, MIN_PQ)

    def insert(self, element):
        if self.min_pq.get_size() < self.k:
            self.min_pq.insert(element)
            return

        if element <= self.min_pq.peek():
            return

        self.min_pq.delete_top()
        self.min_pq.insert(element)

    def get_kth_largest(self):
        return self.min_pq.peek()


# k = KthLargest(3)
# k.insert(2)
# k.insert(3)
# k.insert(1)
# print k.get_kth_largest()
# k.insert(0)
# print k.get_kth_largest()
# k.insert(4)
# k.insert(7)
# print k.get_kth_largest()