import unittest

from challenge_09 import solve, bsearch_row, calc_seat_id
from parameterized import parameterized


class TestChallenge(unittest.TestCase):
    @parameterized.expand([("BFFFBBF", 70), ("FFFBBBF", 14), ("FBFBBFF", 44)])
    def test_bsearch_row(self, inpt, expected):
        s = bsearch_row(inpt)
        self.assertEqual(s, expected)

    def test_calc_seat_id(self):
        inpt = ("BFFFBBF", "RRR")
        expected = 567
        s = calc_seat_id(inpt)
        self.assertEqual(s, expected)
