# How do you check if a string contains only digits?

# Using isdigit
def is_only_digits(s):
    return s.isdigit()


# Example usage
print(is_only_digits("12345"))  # True
print(is_only_digits("1234a5"))  # False

"""

str.isdigit() returns True if all the characters in the string are digits and False otherwise.

"""

# Using isnumeric


def is_only_digits(s):
    return s.isnumeric()


# Example usage
print(is_only_digits("12345"))  # True
print(is_only_digits("1234a5"))  # False

"""

str.isnumeric() returns True if all the characters in the string are digits, or a combination of digits and numeric characters such as +, -, . and it returns False otherwise.

"""

# Using replace


def is_only_digits(s):
    return s.replace(".", "").replace("-", "").replace("+", "").isnumeric()


# Example usage
print(is_only_digits("12345"))  # True
print(is_only_digits("1234a5"))  # False
print(is_only_digits("+12345"))  # True

"""

This method first replaces any "." or "-" or "+" with empty string, then it checks if the resulting string is numeric or not.


"""
