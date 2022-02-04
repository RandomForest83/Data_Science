x = 5
y = "Python"
z = 5.5

print(type(x)) # <class 'int'>
print(type(y)) # <class 'str'>
print(type(z)) # <class 'float'>
print()
#######################################
# Template -> Class
class Teilnehmer:

    # Method
    def greeting(self, name): # (self, name) Parameters
        print("Hallo,", name)

# Create the instances (Copy*)
teilnehmer_1 = Teilnehmer() # Mohamed
teilnehmer_2 = Teilnehmer() # Thomas


# Run the methods
teilnehmer_1.greeting("Mohamed")
teilnehmer_2.greeting("Thomas")

# Check Data Type
print(type(teilnehmer_1)) # <class '__main__.Teilnehmer'>
print(type(teilnehmer_2)) # <class '__main__.Teilnehmer'>

# Compare Instance with class / 'is istance' is a question - comparisson if t_1 has an instance in Teilnehmer
print(isinstance(teilnehmer_1,Teilnehmer)) # True 
print(isinstance(x,Teilnehmer)) # False
