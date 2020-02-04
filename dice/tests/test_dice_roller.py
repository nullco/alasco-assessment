import unittest
from dice.roller import DiceRoller
from tests import FakeDice

class TestDiceRoller(unittest.TestCase):

    def setUp(self):
        self.dice_roller = DiceRoller(
            FakeDice(),
            FakeDice()
        )

    def test_roll(self):
        result = self.dice_roller.roll()
        self.assertEqual(result, 12)