
def calcArea():
  rad = int(input("Enter radius: "))
  return 3.14159 * rad * rad

def calcPerim():
  rad = int(input("Enter radius: "))
  return 2 * 3.14159 * rad

def areaPerim():
  area = calcArea()
  perim = calcPerim()
  return area, perim

def main():
  pie = 3.14159
  rad = int(input("Enter radius: "))
  a, p = areaPerim()
  print(f"Area: {a}\nPerimeter: {p}")

if __name__ == "__main__":
  main()