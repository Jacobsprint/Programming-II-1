class Vehicle:
  def __init__(self, name, tires):
    self.name = name
    self.tires = tires

  def getName(self):
    return self.name + " " + self.tires

class Car(Vehicle):
  def __init__(self, name, tires, worth):
    super().__init__(name, tires)
    self.worth = worth

class Truck(Vehicle):
  def __init__(self, name, tires, miles):
    super().__init__(name, tires)
    self.miles = miles

class Busses(Vehicle):
  def __init__(self, name, tires, city):
    super().__init__(name, tires)
    self.city = city