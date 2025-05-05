

#3. KeyError Handler

try:
  my_dict = {"a": 1, "b": 2}
  print(my_dict["c"])
except KeyError:
  print("Error: Key not found in dictionary")
