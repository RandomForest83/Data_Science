class Participant:

    def __init__(self, name, city, id_number) -> None:
        self.name = name
        self.city = city # public
        self.__id_number = id_number # Private attribute: using double underscore
        self.__banana = 0 # Private attribute

    def greeting(self):
        self.__buchen()
        print(f"Name: {self.name} - ID:{self.__sensitive_data} ")

    def __buchen(self): # Private method
        print("Buchung ist durchgeführt!!")

thomas = Participant("Thomas Meier", "Berlin", "12345")
sara = Participant("Sara Meier", "Frankfurt", "45678")

print(thomas.name)
# print(thomas.id_number) # Error because the id_number is private
# AttributeError: 'Participant' object has no attribute 'id_number'
print(thomas.__dict__) # {'name': 'Thomas Meier', 'city': 'Berlin', '_Participant__id_number': '12345', '_Participant__banana': 0}

print(thomas._Participant__id_number) # I can access private members. 

thomas.name = "Thomas Marc Meier"

print(thomas.__dict__)

thomas._Participant__id_number = "56789"
print(thomas.__dict__)

thomas.greeting()

thomas._Participant__buchen() # POSSIBLE TO ACCESS SENSITIVE DATA! 



"""
Intern method within the class
Extern method outside the class
Sometimes in the extern method the information is sensitive and not to be shown. 
To create a private attribute: __
However as shown below, we can still see private information and that is a Python's downside and
we should be carefull with it. 
Mingling - In Python, mangling is used for class attributes that one does not want subclasses 
to use which are designated as such by giving them a name with two leading underscores and 
no more than one trailing underscore.
"""

