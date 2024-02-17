# Factorial

"""

In simple terms, the factorial of a number is the product of all positive integers up to that number. 
It's denoted by the exclamation mark (!). For example, the factorial of 5, written as 5!, is calculated as:

5!=5x4x3x2x1

- If n is 0 or 1, then the factorial n! is defined to be 1.
- For any other positive integer n, the factorial n! is the product of all positive integers up to n.
- The process is recursive: n! is calculated by multiplying n with the factorial of (n-1), and this process continues until n reaches 0 or 1.

"""

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("Enter a number: "))

result = factorial(num)
print(f"The factorial of {num} is: {result}")