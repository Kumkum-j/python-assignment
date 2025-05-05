#10.Create four modules as list1.py, set2.py, dict3.py, m4.py.
#list1.py
def append1(x,lst):
    lst.append(x)
    return lst

def extend1(l,lst):
    lst.extend(l)
    return lst

def pop1(lst):
    lst.pop()
    return lst

def remove1(x,lst):
    lst.remove(x)
    return lst
