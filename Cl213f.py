class Cl213f:
  def __init__(self, kwh):
    self.kwh = kwh
    self.cost = 0.0

  def calc(self):
    self.cost = 0
    with open("data/prog213f.dat", 'r') as f:
      for line in f:
        kwh = int(line.strip())
        if kwh < 2000:
          self.cost += .07 * kwh
         
        if kwh > 2000 and kwh < 8000:
            self.cost += .05 * 8000
            
        if kwh > 8000:
            self.cost += kwh * .04

  def __str__(self):
    return f"The Cost of {self.kwh} is ${str(self.cost)} "