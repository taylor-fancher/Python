class BankAccount:
    def __init__(self, username, int_rate, balance = 0):
        self.name = username
        self.int_rate = int_rate
        if balance > 0:
            self.balance = balance




taylor = BankAccount('Taylor', .1, 100)
print(taylor.balance)