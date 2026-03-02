class Car:
   def __init__(self, brand, model, year):
      self.brand = brand
      self.model = model
      self.year = year

   def __str__(self):
      return f"{self.year} {self.brand} {self.model}"

# Creating an instance of the Car class
my_car = Car("Toyota", "Corolla", 2021)
my_car2 = Car("Ford", "Mustang", 2009)

# Print the object
print(my_car)  # Output: 2021 Toyota Corolla
print(my_car2)  # Output: 2009 Ford Mustang