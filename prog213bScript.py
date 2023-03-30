def main():
  try:
    with open("data/prog213b.txt", 'r') as f:
      for line in f:
        amount = float(line)
        if amount < 100:
          cost = 5.95
        elif amount >= 100 and amount < 200:
          cost = 5.75
        elif amount >= 200 and amount < 300:
          cost = 5.40
        elif amount >= 300:
          cost = 5.15 
        tc = amount * cost
        cost = float(cost)
        cost = round(cost, 2)
        tc = float(tc)
        tc = round(tc, 2)
        print("Enter Quantity ", str(amount))
        print("Price =", str(cost))
        print("Amount due =", str(tc)) 
        print("\n")
  

  except Exception as e:
    print("Error:", e)

if __name__ == "__main__":
  main()