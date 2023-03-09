from Cl213f import *
def main():
  try:
    elecbill = []
    with open("data/prog213f.dat", 'r') as f:
      for line in f:
        kwh = int(line.strip())
        if kwh != -999:
          bill = Cl213f(kwh)
          elecbill.append(bill)
    for bill in elecbill:
      bill.calc()
      print(bill)

  except Exception as e:
    print("Error:", e)


if  __name__ == "__main__":
  main()
          