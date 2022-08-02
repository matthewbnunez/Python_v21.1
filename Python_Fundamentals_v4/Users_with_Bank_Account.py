class User:
    def __init__(self, first_name, last_name, email, age, gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = gold_card_points
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

    
    def display_info(self):
        print("==========================")
        print(self.first_name, self.last_name, self.email, self.age, self.is_reward_member, self.gold_card_points)
        print("==========================")
        return self


    def enroll(self):
        if(self.is_reward_member != True):
            print(f'{self.first_name} {self.last_name} is now enrolled')
            self.is_reward_member = True
            self.gold_card_points = 200
        else:
            print(f'{self.first_name} {self.last_name} is already enrolled')
        return self


    def spend_points(self, amount):
        if(self.gold_card_points >= amount):
            print("==========================")
            print(f'{self.first_name} {self.last_name} spent {amount} points')
            self.gold_card_points -= amount
            print(f'and now has {self.gold_card_points} points left')
            print("==========================")
        else:
            print("==========================")
            print(f'{self.first_name} {self.last_name} does not have enough points')
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


Matthew = User('Matthew', 'Nunez', 'gmail', 23, 0)
Jim = User('Jim', 'Brown', 'hotmail', 63, 0)
Alex = User('Alex', 'White', 'Yahoomail', 43, 40)

Matthew.enroll().spend_points(150).enroll().display_info().make_deposit(100).display_user_balance()
Jim.enroll().spend_points(80).display_info().make_withdraw(50).display_user_balance()
Alex.spend_points(450).display_info()
