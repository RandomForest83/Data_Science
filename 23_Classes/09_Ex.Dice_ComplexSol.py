from random import randint

class Dice: 

    count_instance = 0 # Class based attribute, Class shared attributes (shared between the instances)

    def __init__(self, side_no = 6) -> None:
        self.side_no = side_no
        Dice.count_instance += 1
        self.cube_id = Dice.count_instance
        
    def roll(self): # A method always needs a self
        # return randint(1,6) hard coded
        return f"Cube_{self.cube_id} Value: {randint(1,self.side_no)}"
cube_list = [] # I can e.g. create a list of dices

cube_1 = Dice()
cube_2 = Dice()
cube_3 = Dice() 

cube_list.append(cube_1)
cube_list.append(cube_2)
cube_list.append(cube_3)

# Create 10x Cubes dynamically
for x in range(10):
    cube = Dice() # Creates a new instance
    cube_list.append(cube) # adds at the end the newly created instances to the list

# Show count of cubes in the list
print(len(cube_list))

# Execute roll() method for all cubes
for cube in cube_list:
    print(cube.roll())

# Reference address
print(cube_1) # <__main__.Dice object at 0x000002A293A86FD0>