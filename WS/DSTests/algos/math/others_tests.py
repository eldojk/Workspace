from unittest import TestCase

from DS.algos.math.others import power


class OthersTestCase(TestCase):

    def test_power(self):
        self.assertEqual(power(5, 5), pow(5, 5))
        self.assertEqual(power(5, 0), 1)
        self.assertEqual(power(5, -5), pow(5, -5))
