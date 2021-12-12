import unittest

from challenge_03 import solve


class TestChallenge(unittest.TestCase):
    def test_solve(self):
        inpt = [("1-3 a", "abcde"), ("1-3 b", "cdefg"), ("2-9 c", "ccccccccc")]
        expected = 2
        s = solve(inpt)
        self.assertEqual(s, expected)
