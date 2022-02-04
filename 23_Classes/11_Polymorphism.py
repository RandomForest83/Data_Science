"""
poly = many
morhpism = forms
"""


# 1. DUCK TYPING
# Duck typing is a concept related to dynamic typing,
# where the type or the class of an object is less important than the methods it defines.
# When you use duck typing, you do not check types at all. 
# Instead, you check for the presence of a given method or attribute.
# IDE = integrated
#~~~~~~~~~~~~~~~~
class VSCode: # Type 1

    def execute(self):
        print("VS code is running perfectly.")

class Jupiter: # Type 2

    def execute(self):
        print("Jupiter is working perfectly.")

class Laptop: # Interface Class
    def run_IDE(self, tool):
        tool.execute()

# Create some instances of the tools
tool_1 = VSCode()
tool_2 = Jupiter()

# Create the Interface Instance
dell_1 = Laptop()

# Send instances to the interface class instance
dell_1.run_IDE(tool_1)
dell_1.run_IDE(tool_2)

print()
####################################################
# 2. Method overriding: Method with the same Name bewteen super calss and child class
#~~~~~~~~~~~~~~~~~~~~~~
class Car: 
    def parking(self):
        print("Car is parking")

class VW(Car):
    def parking(self): # Method overrides the super class implementation
        print("VW is parking")

class Audi(Car):
    pass

vw_1 = VW()
vw_1.parking() # VW is parking

audi_1 = Audi()
audi_1.parking() # Car is parking

####################################################
# 3. Method overloading ----> does NOT exist in Python!!!

def addieren(x,y):
    pass

def addieren(x,y,z):
    pass

addieren(2,3)
addieren(2,3,4)
"""
Monika = "India"
Monika = "DE"
Monika # if we call Monika it will show "DE" because it is the last given information fro the same variable Monika 
"""