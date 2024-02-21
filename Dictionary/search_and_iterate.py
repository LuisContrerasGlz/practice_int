# iterate through a dictionary in Python

my_dict = {'a': 10, 'b': 500, 'c': 200, 'd': 2, 'e': 30, 'f': 80}

# Iterating through keys
for key in my_dict:
    print(key)

# Iterating through values
for value in my_dict.values():
    print(value)

# Iterating through key-value pairs
for key, value in my_dict.items():
    print(f"{key}: {value}")


# --------------- For searching in a dictionary using the in keyword, you can check if a key exists in the dictionary. 

my_dict = {'a': 10, 'b': 500, 'c': 200, 'd': 2, 'e': 30, 'f': 80}

# Searching for a key
key_to_search = 'c'
if key_to_search in my_dict:
    print(f"{key_to_search} is in the dictionary. Its value is {my_dict[key_to_search]}")
else:
    print(f"{key_to_search} is not in the dictionary")

