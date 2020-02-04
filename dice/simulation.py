from dice.game import DiceGame
from dice.player import DiceGamePlayer
from dice.payback import PaybackCalculator
from dice.roller import DiceRoller
from dice.dice import Dice
from tests import FakeDice


def build_player():
    player = DiceGamePlayer(50)
    return player

def build_game():
    dice_roller = DiceRoller(
        Dice(),
        Dice()
    )
    payback_calculator = PaybackCalculator()
    game = DiceGame(dice_roller, payback_calculator)
    return game

def simulate():
    player = build_player()
    game = build_game()
    iterations = 1000

    for _ in range(iterations):
        money = player.grab_money(50)
        payback = game.play_round(money)
        player.store_money(payback)

    if player.get_money() > 0:
        print(f"Play it!, Total euros won after { iterations } iterations: { player.get_money() }")
    else:
        print(f"Don't play it!, total euros lost after { iterations } iterations: { player.get_money() }")

if __name__ == "__main__":
    simulate()