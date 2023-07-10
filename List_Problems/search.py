# Search in a list, python

# With functions or build in methods

# Using the in operator

my_list = [1, 2, 3, 4, 5]
if 3 in my_list:
    print("Element found")
else:
    print("Element not found")

# Using the index() method

my_list = [1, 2, 3, 4, 5]

try:
    index = my_list.index(3)
    print(f"Element found at index {index}")
except ValueError:
    print("Element not found")


# Using a loop

my_list = [1, 2, 3, 4, 5]
target = 3
found = False

for element in my_list:
    if element == target:
        found = True
        break

if found:
    print("Element found")
else:
    print("Element not found")
