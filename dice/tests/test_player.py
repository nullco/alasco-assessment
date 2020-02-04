import unittest
from dice.player import DiceGamePlayer


class TestPlayer(unittest.TestCase):

    def setUp(self):
        self.player = DiceGamePlayer(50)

    def test_money(self):
        self.player.store_money(100)
        self.player.grab_money(50)
        self.player.store_money(300)
        self.player.grab_money(25)
        self.assertEqual(self.player.get_money(), 375)