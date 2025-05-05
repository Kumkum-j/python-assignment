#2 NameError Handler

try:
  print(undefined_variable)
except NameError:
  print("Error: Variable not defined")
