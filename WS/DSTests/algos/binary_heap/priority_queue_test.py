from unittest import TestCase

from DS.algos.binary_heap.priority_queue import PriorityQueue, MAX_PQ, MIN_PQ


class PriorityQueueTest(TestCase):
    def setUp(self):
        self.max_pq = PriorityQueue(10, MAX_PQ)
        self.min_pq = PriorityQueue(10, MIN_PQ)

    def test_max_pq(self):
        self.max_pq.insert(6)
        self.max_pq.insert(1)
        self.max_pq.insert(2)
        self.max_pq.insert(3)

        self.assertEqual(6, self.max_pq.delete_top())
        self.assertEqual(3, self.max_pq.delete_top())
        self.assertEqual(2, self.max_pq.delete_top())
        self.assertEqual(1, self.max_pq.delete_top())

    def test_min_pq(self):
        self.min_pq.insert(6)
        self.min_pq.insert(1)
        self.min_pq.insert(2)
        self.min_pq.insert(3)

        self.assertEqual(1, self.min_pq.delete_top())
        self.assertEqual(2, self.min_pq.delete_top())
        self.assertEqual(3, self.min_pq.delete_top())
        self.assertEqual(6, self.min_pq.delete_top())