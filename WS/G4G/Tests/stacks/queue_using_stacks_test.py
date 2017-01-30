from unittest import TestCase

from G4G.Problems.stacks.queue_using_stacks import Queue


class QueueUsingStackTestCase(TestCase):
    def setUp(self):
        self.q = Queue()

    def test_sorting(self):
        self.q.enqueue(5)
        self.q.enqueue(4)
        self.q.enqueue(88)
        self.q.enqueue(22)

        self.assertEqual(self.q.dequeue(), 5)
        self.assertEqual(self.q.dequeue(), 4)
        self.assertEqual(self.q.dequeue(), 88)
        self.assertEqual(self.q.dequeue(), 22)


