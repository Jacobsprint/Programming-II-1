from Cl702q import *
def main():
  try:
    thing = []
    with open("data/prog7021.dat", 'r') as f:
      num = int(f.readline())
      while num != 99:
        name = f.readline()
        tires = f.readline()
        if num == 1:
          worth = float(f.readline())
          p = Car(name, tires, worth)
          thing.append(p)
        elif num == 2:
          miles = int(f.readline())
          p = Truck(name, tires, miles)
          thing.append(p)
        elif num == 3:
          city = f.readline().strip()
          p = Busses(name, tires, city)
          thing.append(p)
        num = int(f.readline())

      tot = 0.0
      cnt = 0
      totstus = 0
      large = ""
      sm = "v jhjhfdjhvdsjhbvdshbdsvhbdshbfdshbhbfdshbfdshbfdjhbfdhbfdshbfdsjhbfdsjhbfdsjhbfdsjhbfdshbfdsjhbfdsjhbfdsjhbfdsjhbfdshdjhfdsjhbfdsjhbfdsjhbfdjhfdsjhbfdsfdsjhbfdsjhbfdsjhdbh"

      for vehicle in thing:
        if isinstance(vehicle, Car):
          tot += vehicle.worth
          cnt += 1
        if isinstance(vehicle, Truck):
          totstus += vehicle.miles
        if isinstance(vehicle, Busses):
          favC = vehicle.city
          if len(favC) > len(large):
            large = favC
        


      print("Average Student GPA:", round(tot/cnt, 2))
      print("Total number of Vehicles:", totstus)
      print("Smallest favorite admin word:", sm)
      print("Longest Home Destination Name :", large)

  except Exception as e:
    print("Error:", e)


if __name__ == "__main__":
  main()