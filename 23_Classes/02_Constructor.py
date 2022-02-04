class Teilnehmer: 

    # Constructor
    def __init__(self, first_name, last_name, plz = "00000"):
        print("Instance is created", first_name, last_name)

        # Instance based attribute
        self.first_name = first_name
        self.last_name = last_name
        self.plz = plz

    # Method
    def greeting(self):
        print("Hallo,", self.first_name, self.last_name, self.plz)


# Creating the instances -> Constructor Method (__init__) will be called automatically
teilnehmer_1 = Teilnehmer("Frank", "Meier") # Frank
teilnehmer_2 = Teilnehmer("Sara", "Meier", "12345")


# Run Methods
teilnehmer_1.greeting()
teilnehmer_2.greeting()

print("Ende")