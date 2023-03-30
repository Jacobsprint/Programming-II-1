def main():
  np1 = 0
  np2 = 0
  np3 = 0
  np4 = 0
  np5 = 0
  nt = 0
  p1 = 0
  p2 = 0
  p3 = 0
  p4 = 0
  p5 = 0
  try:
    with open("data/prog213e.dat", 'r') as f:
      for age in f:
        age = float(age)
        if age < 20:
          np1 += 1
        elif age >= 20 and age < 40:
          np2 += 1
        elif age >= 40 and age < 60:
          np3 += 1
        elif age >= 60 and age < 80:
          np4 += 1
        elif age >= 80:
          np5 += 1

        nt += 1
        

  except Exception as e:
    print("Error:", e)

  p1 = ( np1 / float(nt)) * 100
  p1 = round(p1,2)
  p2 = ( np2 / float(nt)) * 100
  p2 = round(p2,2)
  p3 = ( np3 / float(nt)) * 100
  p3 = round(p3,2)
  p4 = ( np4 / float(nt)) * 100
  p4 = round(p4,2)
  p5 = ( np5 / float(nt)) * 100
  p5 = round(p5,2)

  print("Age Group Distribution Percentage")
  print("<20 \t\t\t" + str(np1) + "\t\t" + str(p1))
  print("20-39 \t\t\t" + str(np2) + "\t\t" + str(p2))
  print("40-59 \t\t\t" + str(np3) + "\t\t" + str(p3))
  print("60-79 \t\t\t" + str(np4) + "\t\t" + str(p4))
  print(">79\t\t\t\t" + str(np5) + "\t\t" + str(p5))
                                      


if __name__ == "__main__":
  main()