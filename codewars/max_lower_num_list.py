# Program in Python to get the major and lowest number in an array/list

# Using build in functions

def get_major_and_lowest(numbers):
    if not numbers:
        return None, None  # Return None for both major and lowest if the list is empty
    major = max(numbers)
    lowest = min(numbers)
    return major, lowest

# Example usage:
numbers = [3, 7, 1, 9, 5]
major, lowest = get_major_and_lowest(numbers)
print("Major number:", major)
print("Lowest number:", lowest)


# Without build in functions

def get_major_and_lowest_no_build_in(numbers2):

    #  Check if the input list numbers2 is empty, if the list is empty, return None for both major and lowest
    if not numbers2:
        return None, None
    
    # Initialize major_num and lowest_num with the first element of the list
    major_num = numbers2[0]
    lowest_num = numbers2[0]

    # Iterate through each number in the list, Update major_num if the current number is greater than the current major_num and Update lowest_num if the current number is less than the current lowest_num
    for num in numbers2:
        if num > major_num:
            major_num = num
        elif num < lowest_num:
            lowest_num = num

    # Return the major and lowest numbers found
    return major_num, lowest_num

# Testing:
numbers2_check = [3, 7, 1, 9, 5]
major_num, lowest_num = get_major_and_lowest_no_build_in(numbers2_check)
print("Major number:", major_num)
print("Lowest number:", lowest_num)


