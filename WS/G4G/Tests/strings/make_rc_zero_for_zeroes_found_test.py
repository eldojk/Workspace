from unittest import TestCase

from G4G.Problems.strings.make_rc_zero_for_zeroes_found import zero_ify


class ZeroIfyTest(TestCase):
    def setUp(self):
        self.test_matrix = [[1, 2, 3, 0], [2, 3, 4, 5], [3, 0, 5, 6], [8, 9, 7, 5]]
        self.expected_matrix = [[0, 0, 0, 0], [2, 0, 4, 0], [0, 0, 0, 0], [8, 0, 7, 0]]

    def test_zero_ify(self):
        observed = zero_ify(self.test_matrix, 4)
        self.assertSequenceEqual(self.expected_matrix, observed)
