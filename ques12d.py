#12. Package with list1.py, set2.py, dict3.py, m5.py, and m6.py

#__init__.py:

from . import list1
from . import set2
from . import dict3

#m5.py (inside the package, without using __init__.py):

# Importing directly from module paths (without __init__.py)
from .list1 import append1, extend1, pop1, remove1
from .set2 import slen2, adds2, remove2
from .dict3 import len3, add3, keys3, values3

# Using the imported functions (example)
my_list = [1, 2, 3]
my_list = append1(4, my_list)
