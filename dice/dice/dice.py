from random import Random

class Dice:
    
    def __init__(self):
        self.randomizer = Random()

    def roll(self):
        return self.randomizer.randint(1, 6)
    