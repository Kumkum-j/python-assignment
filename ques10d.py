#10.Create four modules as list1.py, set2.py, dict3.py, m4.py.
#m4.py
import list1
import set2
import dict3

my_list = [1, 2, 3]
my_list = list1.append1(4,my_list)  # Appends 4 to my_list
my_list = list1.extend1([5, 6],my_list)  # Extends my_list with [5, 6]
my_list = list1.pop1(my_list)  # Removes the last element
my_list = list1.remove1(2,my_list)  # Removes the element 2

my_set = {1, 2, 3}
set_len = set2.slen2(my_set)  # Gets the length of my_set
my_set = set2.adds2(4,my_set)  # Adds 4 to my_set
my_set = set2.remove2(2,my_set)  # Removes 2 from my_set

my_dict = {"a": 1, "b": 2}
dict_len = dict3.len3(my_dict)  # Gets the length of my_dict
my_dict = dict3.add3("c", 3,my_dict)  # Adds a new key-value pair
keys = dict3.keys3(my_dict)  # Gets the keys of my_dict
values = dict3.values3(my_dict)  # Gets the values of my_dict
