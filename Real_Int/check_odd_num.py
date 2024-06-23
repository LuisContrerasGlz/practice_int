# Check if a number is odd or not in python

def check_odd(num_to_check):
    if num_to_check % 2 == 0:
        print("Number is not Odd")
    else:
        print("Number is Odd")

test = check_odd(7)

"""

The time complexity of the code to check if a number is odd or even is O(1), which is constant time.

The code performs a simple arithmetic operation (num_to_check % 2) and then uses an if statement to check the result.
Regardless of the value of num_to_check, the code performs the same number of operations to determine if it's odd or even. 

Therefore, the time complexity is constant, and it's not dependent on the size or value of num_to_check.

"""

# Adding extra validation

def check_odd(num_to_check):
    if not isinstance(num_to_check, (int, float)):
        print("Input is not a number")
        return
    
    if isinstance(num_to_check, float) and not num_to_check.is_integer():
        print("Input is not an integer")
        return

    if num_to_check % 2 == 0:
        print("Number is not Odd")
    else:
        print("Number is Odd")