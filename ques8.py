#8. ModuleNotFoundError Handler

try:
  import non_existent_module
except ModuleNotFoundError:
  print("Error: Module not found")
