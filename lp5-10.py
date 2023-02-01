num1 = int(input("Enter a Number:"))
num2 = int(input("Enter a Second Number:"))

if num1 < 0 and num2 < 0:
  print("Enter a Positive Number:" )
while num2 > 0:
  temp = num1 % num2
  num1 = num2
  num2 = temp

print("The GCD is: " + str(num1))