class BankAccount:
    def __init__(self, username, int_rate, balance = 0):
        self.name = username
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self,  amount):
        self.balance += amount
        return self
    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
            return self
        else:
            self.balance -= amount
            return self
    def display_account_info(self):
        print(f"Balance: {self.balance}")
        return self
    def yield_interest(self):
        if self.balance > 0:
            yld = self.balance * self.int_rate
            self.balance = self.balance + yld
            return self


Taylor = BankAccount('Taylor', .1, 100)
Chris = BankAccount('Chris', .25, 0)
Taylor.deposit(100).deposit(100) .deposit(100).withdraw(100).yield_interest().display_account_info()
Chris.deposit(500).deposit(500).withdraw(200).withdraw(200).withdraw(200).withdraw(200).yield_interest().display_account_info()