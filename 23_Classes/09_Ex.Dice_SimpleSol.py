from random import randint

class Dice: 
    def roll():
        return randint(1,6)

cube_1 = Dice()

print(Dice.roll())
