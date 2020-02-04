import unittest
from dice.dice import Dice


class TestDice(unittest.TestCase):

    def setUp(self):
        self.dice = Dice()

    def test_roll(self):
        for _ in range(50):
            result = self.dice.roll()
            self.assertTrue(1 <= result <= 6)