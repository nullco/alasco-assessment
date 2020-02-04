class DiceGamePlayer:

    def __init__(self, money):
        self._money = money

    def grab_money(self, amount):
        self._money -= amount
        return amount

    def store_money(self, amount):
        self._money += amount

    def get_money(self):
        return self._money