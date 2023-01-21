# Take a list of numbers, find number of even and odd numbers

def even_odd(lst1):
    evens_num = 0
    odd_num = 0
    for i in range(len(lst1)):
        if i % 2 == 0:
            evens_num += 1
        else:
            odd_num += 1
    return f"You have {evens_num} even numbers, and {odd_num} odd numbers"


print(even_odd([1, 2, 3, 4, 5, 6, 7, 8, 9, 22, 23, 27]))
