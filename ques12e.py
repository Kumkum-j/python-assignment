#12. Package with list1.py, set2.py, dict3.py, m5.py, and m6.py

#m6.py (outside the package, using __init__.py):

# Importing from the package (using __init__.py)
from my_package import list1, set2, dict3

# Using the imported functions (example)
my_list = [1, 2, 3]
my_list = list1.append1(4, my_list)
