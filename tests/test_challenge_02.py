import unittest

from challenge_02 import solve


class TestChallenge(unittest.TestCase):
    def test_solve(self):
        inpt = [1721, 979, 366, 299, 675, 1456]
        expected = 241861950
        s = solve(inpt)
        self.assertEqual(s, expected)
