import random
import numpy as np


def transpose(mat):
  rows = len(mat)
  cols = len(mat[0])
  mat2 = np.empty((rows, cols), dtype = 'int')
  for r in range(5):
    for c in range(5):
      mat2[c][r] = mat[r][c]
  return mat2 


def printMatrix(mat):
  for row in mat:
    for num in row:
      print(f"{num:3d}" , end = "")
    print()


def main():
  mat1 = []
  for r in range(5):
    row1 = []
    for c in range(5):
      rnd1 = random.randint(-50, 99)
      row1.append(rnd1)
    mat1.append(row1)
  printMatrix(mat1)
  print("\n")
  mat2 = transpose(mat1) 
  printMatrix(mat2)
  


if __name__ == "__main__":
  main() 