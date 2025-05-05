
#4. IndexError Handler

try:
  my_list = [1, 2, 3]
  print(my_list[3])
except IndexError:
  print("Error: Index out of range")
