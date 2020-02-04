class PaybackCalculator:

    def calculate_payback(self, money, roll_number):
        if roll_number == 12:
            return money * 4
        elif roll_number == 11:
            return money * 3
        elif roll_number == 10:
            return money * 2
        elif roll_number in [7, 8, 9]:
            return money
        else:
            return 0