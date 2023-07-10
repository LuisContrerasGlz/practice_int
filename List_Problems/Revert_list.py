# Reverse a list 

# With slice:

my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)

# With Loop

def reverse_list(lst):
    left = 0
    right = len(lst) - 1

    while left < right:
        lst[left], lst[right] = lst[right], lst[left]
        left += 1
        right -= 1

    return lst

my_list = [1, 2, 3, 4, 5]
reversed_list = reverse_list(my_list)
print(reversed_list)
