copies = int(input("Enter Number of Copies to be Printed: "))

price = 0 
if copies > 0 and copies <= 99:
  price = .30
elif copies > 99 and copies <= 499:
  price = .28
elif copies > 499 and copies <= 749:
  price = .27
elif copies > 749 and copies <= 1000:
  price = .26
elif copies > 1000:
  price = .25
else:
  print("Number of Copies is Invalid")
print("Price Per Copie is$" + str(price))
print("Total Cost is $" + str(price * copies))