class Employee: 

    # Class based attribute
    bonus = 500

    # Constructor
    def __init__(self, first_name, last_name, plz = "00000"):
        print("Instance is created", first_name, last_name)
# When local value is available its value is taken, otherwise the value from class level (if such existing) is taken. 
        # Instance based attribute
        self.first_name = first_name
        self.last_name = last_name
        self.plz = plz
        self.city = "Berlin" # I cannot change that from outside this class. If I want to make it changable, I need to add it to the attributes in line 7
        self.course_name = ""

    # Method
    def greeting(self):
        print("Hallo,", self.first_name, self.last_name, self.plz)


# Creating the instances -> Constructor Method (__init__) will be called automatically
emp_1 = Employee("Frank", "Meier") # Frank
emp_2 = Employee("Sara", "Meier", "12345")
emp_3 = Employee("Lena", "Meier", "56789")
emp_4 = Employee("Olga", "Henning", "54321")

print("emp_1: ",emp_1.bonus)
print("emp_2: ",emp_2.bonus)
print("emp_3: ",emp_3.bonus)
print("emp_4: ",emp_4.bonus)


# We don't find bonus in the dictionary
print(emp_1.__dict__)
print(emp_2.__dict__)
print(emp_3.__dict__)
print(emp_4.__dict__)

print()
##################################################

emp_1.bonus = 700 # Creates a local value within the attribute

print("emp_1: ",emp_1.bonus)
print("emp_2: ",emp_2.bonus)
print("emp_3: ",emp_3.bonus)
print("emp_4: ",emp_4.bonus)

print(emp_1.__dict__)
print(emp_2.__dict__)
print(emp_3.__dict__)
print(emp_4.__dict__)
print()
###################################################
# Change the value of the class based attribute... ->  via clas itself and not via the instance
Employee.bonus = 1000

print("emp_1: ",emp_1.bonus) # 700 --> local value from the instance
print("emp_2: ",emp_2.bonus) # 1000 --> global class value
print("emp_3: ",emp_3.bonus) # 1000
print("emp_4: ",emp_4.bonus) # 1000

print(emp_1.__dict__)
print(emp_2.__dict__)
print(emp_3.__dict__)
print(emp_4.__dict__)