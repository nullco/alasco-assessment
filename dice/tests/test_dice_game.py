import unittest
from dice.roller import DiceRoller
from dice.game import DiceGame
from dice.payback import PaybackCalculator
from tests import FakeDice

class TestDiceRoller(unittest.TestCase):

    def setUp(self):
        dice_roller = DiceRoller(
            FakeDice(),
            FakeDice()
        )
        payback_calculator = PaybackCalculator()
        self.game = DiceGame(dice_roller, payback_calculator)

    def test_round(self):
        result = self.game.play_round(0.5)
        self.assertEqual(result, 2)