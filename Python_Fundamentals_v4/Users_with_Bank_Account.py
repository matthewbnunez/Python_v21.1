class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = BankAccount(int_rate = 0.02, balance = 0)

    def make_deposit(self, amount):
        self.account.deposit(amount)
        return self

    def make_withdraw(self, amount):
        self.account.withdraw(amount)
        return self

    def display_user_balance(self):
        self.account.display_account_info()
        return self

    



class BankAccount:
    # don't forget to add some default values for these parameters!
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    def deposit(self, amount):
        print(f'You are depositing ${amount} in your account')
        self.balance += amount
        return self

    def withdraw(self, amount):
        print(f'You are withdrawing ${amount} in your account')
        self.balance -= amount
        return self

    def display_account_info(self):
        print(f'Your account balance is ${self.balance}')
        return self

    def yield_interest(self):
        self.balance += self.balance * self.int_rate
        print(f'You have gained interest your account balance is now ${self.balance}')
        return self


Matthew = User('Matthew', 'gmail')
Jim = User('Jim', 'hotmail')

Matthew.make_deposit(100).display_user_balance()
Jim.make_withdraw(50).display_user_balance()
