class User:
    def __init__(self, first_name, last_name, email, age, gold_card_points):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_reward_member = False
        self.gold_card_points = gold_card_points
    
    def display_info(self):
        print(self.first_name, self.last_name, self.email, self.age, self.is_reward_member, self.gold_card_points)

    def enroll(self):
        if(self.is_reward_member != True):
            self.is_reward_member = True
            self.gold_card_points = 200
        else:
            print(f'{self.first_name} {self.last_name} is already enrolled')

    def spend_points(self, amount):
        if(self.gold_card_points >= amount):
            print(f'{self.first_name} {self.last_name} spent {amount} points')
            self.gold_card_points -= amount
            print(f'and now has {self.gold_card_points} points left')
        else:
            print(f'{self.first_name} {self.last_name} does not have enough points')

Matthew = User('Matthew', 'Nunez', 'gmail', 23, 0)
Jim = User('Jim', 'Brown', 'hotmail', 63, 0)
Alex = User('Alex', 'White', 'Yahoomail', 43, 40)

User.enroll(Matthew)
Matthew.spend_points(150)
User.enroll(Jim)
Jim.spend_points(80)
User.enroll(Matthew)
Alex.spend_points(450)

User.display_info(Matthew)
User.display_info(Jim)
User.display_info(Alex)