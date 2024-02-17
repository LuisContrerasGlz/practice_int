# Fibonacci

# The Fibonacci series is a sequence of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. 


a, b = 0, 1
while a <= 10:
    print(a, end=" ")
    a, b = b, a + b

# With input
    
a, b = 0, 1
n = int(input("Enter the number for the Fibonacci series: "))
while a <= n:
    print(a, end=" ")
    a, b = b, a + b