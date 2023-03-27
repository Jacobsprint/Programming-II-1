import sys
sys.setrecursionlimit(5000)

def fact(n):
  if n == 3: 
    return n 
  return n * fact(n-3)

def main():
  np = 0
  for num in range(3, 9669+1, 3):
    np += num
  print("The sum of the multiples of 3, from 3 to 9669 is", int(np))
    
if __name__ == "__main__":
  main()