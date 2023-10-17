# Write a function that will print tell the user if a number is divisible by 8, 16, or 32.

def tell_div(numtocheck):
    if numtocheck % 8 == 0 or numtocheck % 16 == 0 or numtocheck % 32 == 0:
        return "Your number is divisible by 8, 16 or 32"
    else:
        return "Sorry, Your number is not divisible by 8, 16 or 32"


print(tell_div(80))

"""

The time complexity of the code provided to check if a number is divisible by 8, 16, or 32 is O(1), which is constant time.

The code performs a series of modulo operations (numtocheck % 8, numtocheck % 16, and numtocheck % 32) and evaluates the result within an if statement. Regardless of the value of numtocheck, the code always performs the same number of operations to determine if it's divisible by 8, 16, or 32. 

Therefore, the time complexity is constant, and it's not dependent on the size or value of numtocheck.

"""