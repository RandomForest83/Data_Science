class Teilnehmer: 

    # Constructor
    def __init__(self, first_name, last_name, plz = "00000"):
        print("Instance is created", first_name, last_name)

        # Instance based attribute
        self.first_name = first_name
        self.last_name = last_name
        self.plz = plz
        self.salary = 0


    # Method
    def greeting(self):
        print("Hallo,", self.first_name, self.last_name, self.plz)


# Creating the instances -> Constructor Method (__init__) will be called automatically
teilnehmer_1 = Teilnehmer("Frank", "Meier") # Frank
teilnehmer_2 = Teilnehmer("Sara", "Meier", "12345")


# Show the attributes within the instance using __dict__
print(teilnehmer_1.__dict__)
print(teilnehmer_2.__dict__)

# Show values of attributes
print(teilnehmer_1.first_name)
print(teilnehmer_2.last_name)

# Change a value of an attribute
teilnehmer_1.plz = "11111"
print(teilnehmer_1.plz)

print(teilnehmer_1.__dict__)
print(teilnehmer_2.__dict__)

# WARNING!!! In Python you can create directly a new attribute via the instance
teilnehmer_1.banana = "300g"
print(teilnehmer_1.banana)

teilnehmer_2.car = "Audi"
print(teilnehmer_1.__dict__)
print(teilnehmer_2.__dict__)

# SO teilnehmer_1 has "banana" and teilnehmer_2 has "car"
print()

########################################################
teilnehmer_list = []
teilnehmer_list.append(teilnehmer_1)
teilnehmer_list.append(teilnehmer_2)

for teilnehmer in teilnehmer_list: 
    print(f"Teilnehmer: {teilnehmer.first_name} {teilnehmer.last_name}")