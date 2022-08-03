import Parent
Ninja = Parent.Ninja

class Pet():
    def __init__(self, name , type , tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.energy = 60
        self.health = 90

    def sleep(self):
        self.energy += 25

    def eat(self):
        self.energy += 5
        self.health += 10
        print('Cat ate some food')

    def play(self):
        self.health += 5
        print('Cat played around')

    def noise(self):
        print('moew')

class Tabby(Pet):
    def __init__(self, name , type , tricks):
        super().__init__(name, type, tricks)

class Tabby(Pet):
    def __init__(self, name , type , tricks):
        super().__init__(name, type, tricks)

class Tabby(Pet):
    def __init__(self, name , type , tricks):
        super().__init__(name, type, tricks)
    # implement the following methods:
    # sleep() - increases the pets energy by 25
    # eat() - increases the pet's energy by 5 & health by 10
    # play() - increases the pet's health by 5
    # noise() - prints out the pet's sound

CoCo = Tabby('Coco' , 'tabby' , 'play dead')
ChuChu = Tabby('DD' , 'Maine Coon' , 'play dead')
LuLu = Tabby('LuLu' , 'Scottish Fold' , 'play dead')

Jim = Ninja('Jim', 'Bob', 'Wet food', 'Dry food', CoCo)
Mike = Ninja('Mike', 'Mason', 'Raw Chicken', 'Wet food', ChuChu)
Robert = Ninja('Robert', 'White', 'Treats', 'Dry food', LuLu)

Jim.feed().walk().bathe()
Mike.feed().walk().bathe()
Robert.feed().walk().bathe()