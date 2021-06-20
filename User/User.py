class user:
    def __init__(self, username):
        self.name = username
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawl(self, amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print(self.account_balance)
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount

Paul = user('Paul')
Paul. make_deposit(500)
Paul.display_user_balance()
Steve = user('Steve')
Steve.make_deposit(500)
Steve.display_user_balance()
Paul.transfer_money(Steve, 250)
Paul.display_user_balance()
Steve.display_user_balance()