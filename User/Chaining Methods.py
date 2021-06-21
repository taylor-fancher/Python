class user:
    def __init__(self, username):
        self.name = username
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.account_balance)
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

Paul = user('Paul')
Sam = user('Sam')
Bob = user('Bob')
Paul.make_deposit(100).make_deposit(100).make_deposit(100).make_withdrawl(150).display_user_balance()
Sam.make_deposit(200).make_deposit(200).make_withdrawl(75).make_withdrawl(75).display_user_balance()
Bob.make_deposit(500).make_withdrawl(100).make_withdrawl(100).make_withdrawl(100).display_user_balance()
Paul.transfer_money(Bob, 100).display_user_balance()
Bob.display_user_balance()