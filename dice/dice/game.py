class DiceGame:

    def __init__(self, dice_roller, payback_calculator):
        self.dice_roller = dice_roller
        self.payback_calculator = payback_calculator

    def play_round(self, money):
        roll_output = self.dice_roller.roll()
        return self.payback_calculator.calculate_payback(money, roll_output)