# Ordered Dictionary

"""

An OrderedDict is a dictionary subclass that maintains the order in which items are inserted. 
Unlike a regular dictionary, which does not guarantee any specific order of items, an OrderedDict keeps track of the order in which key-value pairs are added.

"""
from collections import OrderedDict

od = OrderedDict()
od["a"] = 10
od["b"] = 500
od["c"] = 200
od["d"] = 2
od["e"] = 30
od["f"] = 80

print(od)

# Other ways to make an OrderedDict

# Passing a List of Tuples:

items = [('a', 10), ('b', 500), ('c', 200), ('d', 2), ('e', 30), ('f', 80)]
od = OrderedDict(items)
print(od)

# Using a Dictionary:

my_dict = {'a': 10, 'b': 500, 'c': 200, 'd': 2, 'e': 30, 'f': 80}
od = OrderedDict(my_dict)
print(od)