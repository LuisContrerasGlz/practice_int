# Write a function that will print tell the user if a number is divisible by 8, 16, or 32.

def tell_div(numtocheck):
    if numtocheck % 8 == 0 or numtocheck % 16 == 0 or numtocheck % 32 == 0:
        return "Your number is divisible by 8, 16 or 32"
    else:
        return "Sorry, Your number is not divisible by 8, 16 or 32"


print(tell_div(80))
