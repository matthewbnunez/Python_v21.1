class BankAccount:
    # don't forget to add some default values for these parameters!
    all_accounts = []
    def __init__(self, int_rate, balance): 
        self.int_rate = int_rate
        self.balance = balance
        BankAccount.all_accounts.append(self)
        # your code here! (remember, instance attributes go here)
        # don't worry about user info here; we'll involve the User class soon
    @classmethod
    def print_all_accounts(cls):
        for one_account in cls.all_accounts:
            print(f'Interest Rate: {one_account.int_rate} Balance: {one_account.balance}')

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

Jake = BankAccount(.05, 2650)
Mike = BankAccount(.02, 736050)
Bob = BankAccount(.12, 150)

Jake.deposit(200).deposit(300).deposit(150).withdraw(50).display_account_info().yield_interest()
Mike.deposit(13000).deposit(8000).withdraw(5000).withdraw(1000).withdraw(4000).withdraw(50000).display_account_info().yield_interest()

BankAccount.print_all_accounts()