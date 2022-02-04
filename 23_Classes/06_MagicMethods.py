# https://rszalski.github.io/magicmethods/

class Car: 
    def __init__(self, model, kz, km, price) -> None: # -> Annotation
        self.model = model
        self.kz = kz
        self.km = km
        self.price = price

    def show_data(self):
        print(f"Model:  {self.model} - KZ:{self.kz}")

    def print_data(self):
        return f"Model:  {self.model} - KZ:{self.kz}"

    def __str__(self): # Converts an object to string --> E.g. the object Car into a string
        return f"Model:  {self.model} - KZ:{self.kz}"  

    def __gt__(self, other): # gt=greater than self is not changeble, but other can be anything
        return self.price > other.price

    def __eq__(self, other): # equal
        return self.price == other.price


# Creating an Instance
tiguan = Car("Toguan", "AA123445", 5000, 15000)
touran = Car("Touran", "BB123456", 7000, 14000)


print(tiguan) # Model:  Toguan - KZ:AA123445
# If it wasn't defined with show_data it would print the address: <__main__.Car object at 0x000001F0D9255EB0>
print(touran) # <__main__.Car object at 0x00000216CE3B5940>


tiguan.show_data()
touran.show_data()

print(tiguan.print_data())
print(touran.print_data())


print(tiguan)
print(touran)
print()

#####################################
print(tiguan> touran) # True
print(tiguan == touran) # False