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
