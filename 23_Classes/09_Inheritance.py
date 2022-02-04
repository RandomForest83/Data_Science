# INHERITANCE / VERERBUNG
# Super class
class Car:
    def __init__(self, model, kz, km) -> None:
        self.model = model
        self.kz = kz
        self.km = km

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

class Audi(Car):
    
    def __init__(self, model, kz, km, panorama) -> None:
        super().__init__(model, kz, km)
        self.panorama = panorama

    def panorama_open(self):
        print("Panorama is opening...")

class Tesla(Car):
    def __init__(self, model, kz, km, battery) -> None:
        super().__init__(model, kz, km)
        self.battery = battery

        def battery_charge(self):
            print("Battery is charging...")


# Create instances
vw_1 = VW("Passat", "AA12345", 5000, True)
audi_1 = Audi("Passat", "BB12345", 6000, True)
tesla_1 = Tesla("Passat", "CC12345", 7000, True)

list_car = [vw_1, audi_1, tesla_1]

for car in list_car:
    car.drive()
print() # Empty line

for car in list_car:
    car.park()

for car in list_car:
    car.clean()



































# Inheritance / Vererbung
# Super Class
