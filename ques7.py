#7. FileNotFoundError Handler

try:
  with open("nonexistent_file.txt", "r") as file:
    content = file.read()
except FileNotFoundError:
  print("Error: File not found")
