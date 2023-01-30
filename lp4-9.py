import random
player = int(input("Pick a Number between 1 and 20: "))


num = random.randint(0, 21)

print("Computer's Number : " + str(num))
print("Player's Number: " + str(player))

if num == player:
  print("You Won!!!")
else:
  print("Better Luck Next Time")




