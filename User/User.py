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
Sam = user('Sam')
Bob = user('Bob')
Paul.make_deposit(100)
Paul.make_deposit(100)
Paul.make_deposit(100)
Paul.make_withdrawl(150)
Paul.display_user_balance()
Sam.make_deposit(200)
Sam.make_deposit(200)
Sam.make_withdrawl(75)
Sam.make_withdrawl(75)
Sam.display_user_balance()
Bob.make_deposit(500)
Bob.make_withdrawl(100)
Bob.make_withdrawl(100)
Bob.make_withdrawl(100)
Bob.display_user_balance()
Paul.transfer_money(Bob, 100)
Paul.display_user_balance()
Bob.display_user_balance()