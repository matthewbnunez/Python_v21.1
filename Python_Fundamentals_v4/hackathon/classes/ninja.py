
from classes.character import Character

class Ninja(Character):
    def __init__(self):
        super().__init__()  #adds atriubutes from previos construct
        self.stam = 10
        self.defense = 10
        self.weapon = 7

    def attack(self, target):
        print(f"nothing personal kid")
        damage = self.strength + self.weapon - target.defense
        target.health -= damage
        """
        roll = random.randint(1,15)
        if (roll > 10):
            target.health -= self.weapon_damage
"""
    def stunned(self, target):
        print("stun't")
        yeet = True
        target.stun = yeet
