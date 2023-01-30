numeggs = int(input("Number of Eggs Purchased: "))

price = 0
bill = 0

numdoz = numeggs / 12

if numdoz > 0 and numdoz <= 4:
  price = 0.0416
elif numdoz < 4 and numdoz >= 6:
  price = 0.0375
elif numdoz < 6 and numdoz <= 11:
  price = 0.0333
elif numdoz > 11:
  price = 0.0291

bill = price * numeggs
bill = round(bill, 2)
print("The Bill is Equal to $" + str(bill))