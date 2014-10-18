class CashDesk:
    def __init__(self):
        self.money = {100: 0, 50: 0, 20: 0, 10: 0, 5: 0, 2: 0, 1: 0}

    def take_money(self, money):
        for key in money:
            self.money[key] += money[key]

    def total(self):
        total_sum = 0
        for key in self.money:
            total_sum += key * self.money[key]
        return total_sum

    def can_withdraw_money(self, amount_of_money):
        money_diction = {}
        for key in self.money:
            if self.money[key] != 0:
                money_diction[key] = self.money[key]
        for key in sorted(money_diction, reverse=True):
            while amount_of_money - key >= 0 and money_diction[key] > 0:
                amount_of_money -= key
                money_diction[key] -= 1
        if amount_of_money == 0:
            return True
        else:
            return False




def main():
    my_cash_desk = CashDesk()
    my_cash_desk.take_money({1: 2, 50: 2, 20: 1})
    print(my_cash_desk.money)
    print(my_cash_desk.total())


if __name__ == '__main__':
    main()
