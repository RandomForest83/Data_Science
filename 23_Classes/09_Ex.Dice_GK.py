from random import randint

class Dice:
    def __init__(self, number_sides = 6):
        self.number_sides = number_sides

    def roll_the_dice(self): 
        print("Roll the dices...")
        number = randint(1,self.number_sides)
        print(f"Your number: {number}")
cube1 = Dice() # Instance from the Dice
cube2 = Dice() 

cube1.roll_the_dice()
cube2.roll_the_dice()


""" Python has a built-in module that you can use to make random numbers.
The random module has a set of methods.
We need that when we want to teach the software to other possibilities. 
Machine learning - to try something out. 
"""