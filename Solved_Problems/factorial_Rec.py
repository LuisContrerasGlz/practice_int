# Find the factorial, using recursion

# Defining a function called factorial
def factorial(n):
    # Defining the base case
    if n < 2:
        return 1
    # Recursive case
    return n * factorial(n-1)


# Note, the maxim limit of recursion calls in python is 1000
print(factorial(5))
