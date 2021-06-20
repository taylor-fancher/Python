class BankAccount:
    def __init__(self, username, int_rate, balance):
        self.name = username
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self,  amount):
        self.balance += amount
    def withdraw(self, amount):
        if amount > self.balance:
            print('Insufficient funds: Charging a $5 fee')
            self.balance -= 5
        else:
            self.balance -= amount
    def display_account_info(self):
        print(f"Balance: {self.balance}")
    def yield_interest(self):
        if self.balance > 0:
            yld = self.balance * self.int_rate
            self.balance = self.balance + yld


Taylor = BankAccount('Taylor', .1, 100)
Taylor.display_account_info()
Taylor.yield_interest()
Taylor.display_account_info()
