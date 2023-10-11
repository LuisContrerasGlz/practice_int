# Traverse from back to front in a given array.

array_to_traverse = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

# Declaring a back variable which starts at -1
back = -1

# Looping the array from -1 and add -1 to that until we finish
for i in range(len(array_to_traverse)):
    print(array_to_traverse[back])
    back -= 1
