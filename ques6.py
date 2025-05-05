#6. AttributeError Handler

try:
    x = 10
    x.append(5)
except AttributeError:
    print("Error: Attribute does not exist")
