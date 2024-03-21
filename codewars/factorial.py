# Create a program to calculate the factorial, recursive

def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n-1)
    
print(factorial(5))

# 1 x 2 x 3 x 4 x 5 = 120