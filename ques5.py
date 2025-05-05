#5. ValueError Handler

try:
  int("abc")
except ValueError:
  print("Error: Invalid value for data type conversion")
