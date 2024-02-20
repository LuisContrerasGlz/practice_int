"""

List comprehensions are a concise and readable way to create lists in Python. 
They provide a more compact syntax for creating lists by applying an expression to each item in an existing iterable (such as a list, tuple, or range) 
and optionally filtering the items based on a condition.

new_list = [expression for item in iterable if condition]

expression: The expression to be evaluated for each item.
item: The variable representing each item in the iterable.
iterable: The existing iterable (e.g., list, tuple, range) to iterate over.
condition (optional): An optional condition to filter items.

"""

# Basic list comprehension:

squares = [x**2 for x in range(5)]
# Output: [0, 1, 4, 9, 16]

# List comprehension with a condition:
even_squares = [x**2 for x in range(10) if x % 2 == 0]
# Output: [0, 4, 16, 36, 64]

# Nested list comprehension:

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [element for row in matrix for element in row]
# Output: [1, 2, 3, 4, 5, 6, 7, 8, 9]


