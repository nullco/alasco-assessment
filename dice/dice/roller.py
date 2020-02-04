class DiceRoller:

    def __init__(self, *args):
        self.dice = args

    def roll(self):
        return sum([dice.roll() for dice in self.dice])
