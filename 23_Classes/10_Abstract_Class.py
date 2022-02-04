"""
Native Python does NOT have abstract class, therefore we use the built-in module ABC. 

Abstract CLass: A class which can NOT be initiated. 
~~~~~~~~~~~~~~

Requirements:
~~~~~~~~~~~~~~
1. Abstract class should inherite from abc class
2. Minimum one abstract method in the abstract class

Benefits:
~~~~~~~~~
1. Disable initial, an abstract class.
2. Make sure that every child class has an implementation of abstract method. 
"""
from abc import ABC, abstractmethod

# with (ABC) we make the Super Class Car abstract 
class Car(ABC):
    def __init__(self, model, kz, km) -> None:
        self.model = model
        self.kz = kz
        self.km = km

    @abstractmethod
    def test(self):
        raise NotImplementedError("Please implement in the child class.")

    @abstractmethod
    def anmelden(self):
        raise NotImplementedError("Please implement in the child class.")
# Error types https://docs.python.org/3/library/exceptions.html 

    def drive(self):
        print("Car is driving perfectly!")

    def park(self):
        print("Car is parking...")

    def clean(self):
        print("Car is cleaned.")

# Class
class VW(Car): 

    def __init__(self, model, kz, km, gps) -> None: # Receiving // model, kz, km, gps --> parameters of VW
        super().__init__(model, kz, km) # Calling // model, kz, km --> arguments of the super class Car
        self.gps = gps

    def gps_navi(self):
        print("GPS is navigating")
    
    def test(self):
        print("This is VW test.")

    def anmelden(self):
        print("This is VW Anmeldung.")

class Audi(Car):
    
    def __init__(self, model, kz, km, panorama) -> None:
        super().__init__(model, kz, km)
        self.panorama = panorama

    def panorama_open(self):
        print("Panorama is opening...")

    def test(self):
        print("This is Audi test.")

    def anmelden(self):
        print("This is Audi Anmeldung.")

class Tesla(Car):
    def __init__(self, model, kz, km, battery) -> None:
        super().__init__(model, kz, km)
        self.battery = battery

        def battery_charge(self):
            print("Battery is charging...")

    def test(self):
        print("This is Tesla test.")

    def anmelden(self):
        print("This is Tesla Anmeldung.")


# Create instances
vw_1 = VW("Passat", "AA12345", 5000, True)
audi_1 = Audi("Passat", "BB12345", 6000, True)
tesla_1 = Tesla("Passat", "CC12345", 7000, True)

vw_1.drive()

vw_1.anmelden()
audi_1.anmelden()
tesla_1.anmelden()
