from unittest import TestCase

from G4G.Problems.binary_heap.running_median import RunningMedian


class RunningMedianTest(TestCase):
    def setUp(self):
        self.median_resolver = RunningMedian()

    def test_running_median(self):
        self.median_resolver.add(3)
        self.assertEqual(float(self.median_resolver.get_median()), 3.00)

        self.median_resolver.add(5)
        self.assertEqual(float(self.median_resolver.get_median()), 4.00)

        self.median_resolver.add(7)
        self.assertEqual(float(self.median_resolver.get_median()), 5.00)

        self.median_resolver.add(1)
        self.assertEqual(float(self.median_resolver.get_median()), 4.00)

        self.median_resolver.add(0)
        self.assertEqual(float(self.median_resolver.get_median()), 3.00)

        self.median_resolver.add(9)
        self.assertEqual(float(self.median_resolver.get_median()), 4.00)
