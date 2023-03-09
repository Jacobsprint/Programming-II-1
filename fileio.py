lines = ["Hello, ", "World", "!"]

#File write mode 'w' is "overright" by default, use 'a' for append
with open("data/nyfile.txt", 'w') as f:
  #Writing data to a file
  f.write("Hi \n")
  f.writelines(lines)
  # or, for line in lines: file.write(line)

write open("data/nyfile.txt", 'r') as f:
#Reading from a file 
  print(f.read())