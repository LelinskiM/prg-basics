class Car:
 def __init__(self, brand, model, year):
     self.brand = brand  # Object attribute
     self.model = model  # Object attribute
     self.year = year    # Object attribute

 def display_info(self):
     print(f"Car: {self.brand} {self.model}, Year: {self.year}")

f = Car("ford", "mustang", 2020)
f.display_info()

my_car = Car("Toyota", "Corolla", 2021)  # Creating an object of the Car class
my_car.display_info()  # Calling a method on the object