# Reverse a list 

# With slice:

my_list = [1, 2, 3, 4, 5]
reversed_list = my_list[::-1]
print(reversed_list)

# With Loop, reverse the elements of a list in-place without using additional memory, two-pointer technique to swap the elements at the beginning and end of the list iteratively.

def reverse_list_in_place(lst):
    start = 0
    end = len(lst) - 1

    while start < end:
        lst[start], lst[end] = lst[end], lst[start]
        start += 1
        end -= 1

# Example usage
my_list = [1, 2, 3, 4, 5]
reverse_list_in_place(my_list)
print(my_list)  # Output: [5, 4, 3, 2, 1]

