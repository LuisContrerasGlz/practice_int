"""

The filter() function in Python is used to filter a sequence (like a list) by applying a given function to each element of the sequence. 
It returns a new sequence containing only the elements for which the function returns True.

filter(function, iterable)

function: The function that tests each element of the iterable. It should return either True or False.
iterable: The sequence (e.g., a list) to be filtered.

So, in simple terms, filter() helps you create a new sequence with only the elements that satisfy a specific condition defined by a given function.

"""

def add7(num):
    return num+7

def is_odd(num2):
    return num2 % 2 != 0

a = [1,2,3,4,5,6,7,8,9,10]
b = list(filter(is_odd,a))

print(a)
print(b)

# Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even(num):
    return num % 2 == 0

even_numbers = filter(is_even, numbers)
print(list(even_numbers))
