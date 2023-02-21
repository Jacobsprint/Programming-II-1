class ClLp312:
  def __init__(self, ds, cd, db, tt):
    self.design = ds
    self.coding = cd
    self.debug = db
    self.testing = tt
    self.task = 0
    self.percents = [0]*4 #[0,0,0,0]

  def _percent(self, number):
    return round((number / self.task) * 100, 2)

  def calculate(self):
    self.task = self.design + self.coding + \
                  self.debug + self.testing
    self.percents[0] = self._percent(self.design)
    self.percents[1] = self._percent(self.coding)
    self.percents[2] = self._percent(self.debug)
    self.percents[3] = self._percent(self.testing)

  def display(self):
    print("Category\tTask")
    print(f"Designing\t{self.percents[0]}%")
    print(f"Coding\t\t{self.percents[1]}%")
    print(f"Debuging\t{self.percents[2]}%")
    print(f"Testing\t\t{self.percents[3]}%")


def main():
  print("Enter the amount of time spent on the following tasks in hours: \n")
  design = float(input("Designing: "))
  coding = float(input("Coding: " ))
  debug = float(input("Debuging: " ))
  testing = float(input("Testing: " ))
  print()
  
  #Make a new "ClLp312" object, pass in numbers to the constructor
  task = ClLp312(design,coding,debug,testing)
  task.calculate()
  task.display()

if __name__ == "__main__":
  main()