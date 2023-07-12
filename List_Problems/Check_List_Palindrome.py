# Check if a given list is a palindrome (reads the same forwards and backwards).

def is_palindrome(lst):
    return lst == lst[::-1]

# Example usage
list1 = [1, 2, 3, 2, 1]
print(is_palindrome(list1))  # Output: True

list2 = [1, 2, 3, 4, 5]
print(is_palindrome(list2))  # Output: False
