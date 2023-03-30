def main():
  nl = 0
  nm = 0
  nt = 0
  try:
    with open("data/prog215a.dat", 'r') as f:
      for num in f:
        nt += 1
        if int(num) < 500:
          nl += 1
        else: 
          nm += 1
      


  except Exception as e:
    print("Error:", e)

  print("The number of numbers less than 500 is", int(nl))
  print("The number of numbers greater than or equal to 500 is", int(nm))
  print("The total number of numbers is", int(nt))

if __name__ == "__main__":
  main()