# Check for the largest number in an array 

# With function

my_list = [10, 5, 7, 22, 13, 19]
largest_number = max(my_list)
print(largest_number)

# Without function

def find_largest_number(lst):
    largest = float('-inf')  # Initialize with negative infinity

    for num in lst:
        if num > largest:
            largest = num

    return largest

# Example usage
my_list = [10, 5, 7, 22, 13, 19]
largest_number = find_largest_number(my_list)
print(largest_number)
