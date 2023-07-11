# Sort a list

# With function and methods

# Sorts in place

my_list = [3, 1, 4, 2, 5]
my_list.sort()
print(my_list)

# Creates a new list without modifying the orignal

my_list = [3, 1, 4, 2, 5]
sorted_list = sorted(my_list)
print(sorted_list)

"""
Both methods will sort the list in ascending order. 
If you want to sort the list in descending order, you can pass the reverse=True argument to either sort() or sorted() functions. 
"""

my_list = [3, 1, 4, 2, 5]
my_list.sort(reverse=True)
print(my_list)

my_list = [3, 1, 4, 2, 5]
sorted_list = sorted(my_list, reverse=True)
print(sorted_list)


# Without function or methods

# Bubble sort, O(n^2), where n is the number of elements in the list. 

def bubble_sort(lst):
    n = len(lst)

    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    return lst

# Example usage
my_list = [3, 1, 4, 2, 5]
sorted_list = bubble_sort(my_list)
print(sorted_list)


