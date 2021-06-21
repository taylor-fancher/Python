class BankAccount:
    def __init__(self, username, int_rate, balance = 0):
        self.name = username
        self.int_rate = int_rate
        if balance > 0:
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

class user:
    def __init__(self, username):
        self.name = username
        self.account = BankAccount(int_rate=0.02, balance=0)
    def make_deposit(self, amount):
        self.account.deposit(amount)
    def make_withdrawl(self, amount):
        self.account.withdraw(amount)
    def display_user_balance(self):
        self.account.display_account_info
    def transfer_money(self, other_user, amount):
        self.account.withdraw(amount)
        other_user.account.deposit(amount)