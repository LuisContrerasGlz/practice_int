"""
    EXPLANATION:
 
    1) The coding exercise consist on two main things
        - Of a given arrays, remove duplicates on both
        - Print the arrays in three different ways:
            1. Original collection
            2. Collection with duplicates removed
            3. Collection with duplicates removed and sorted


"""

arrOne = [2, 5, 5, 55, 69, 666, 666, 2019, 42, 21, 9, 2, 69, 5]
arrTwo = ["John", "Tina", "Tom", "Jonah", "Laura", "Tina", "Bob", "Bob", "Robert", "John", "Tina", "Tom", "Mike"]
# Print Original collection
print(arrOne)
print(arrTwo)
    
# Collection with duplicates removed
newarrOne = set(arrOne) 
print(list(newarrOne))
    
newarrTwo = set(arrTwo) 
print(list(newarrTwo))
    
# Collection with duplicates removed and sorted
list(newarrOne).sort()
list(newarrTwo).sort()

# with  for
newarrOne = []
for i in arrOne:
    if i not in newarrOne:
        newarrOne.append(i)

print(newarrOne)

newarrTwo = []    
for i in arrTwo:
    if i not in newarrTwo:
        newarrTwo.append(i)
print(newarrTwo)
