class Vehicle:
    def __init__(self,brand: str, year:int) -> None:
        self.brand = brand
        self.year = year

    def start_car(self):
        print("The car is started")

    
class ElectricCar(Vehicle):
    def __init__(self, brand: str, year: int, battery_size: int) -> None:
        super().__init__(brand, year) # Super() is to Get  The Data from parent
        self.battery_size = battery_size

    def start_car(self): # here Override
        print("The Battery is Started")

    
e =  ElectricCar("Tesla",2020,5000)

print(e.battery_size)
print(e.brand)
e.start_car()
