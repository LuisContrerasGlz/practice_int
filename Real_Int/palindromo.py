# Create a function to check if a string is palindrom 

def is_palindrome(input_string):
    # Remove spaces and convert the input string to lowercase
    input_string = input_string.replace(" ", "").lower()
    
    # Compare the input string with its reverse
    if input_string == input_string[::-1]:
        print("Palindrome")
        return True
    else:
        print("Not palindrome")
        return False

# Example usage:
input_str = "A man a plan a canal Panama"
result = is_palindrome(input_str)

"""

The time complexity (big O notation) of the provided palindrome-checking code is O(n), where 'n' is the length of the input string.

Here's the breakdown of the time complexity:

The code begins by removing spaces and converting the input string to lowercase. Both of these operations have time complexities of O(n), where 'n' is the length of the input string. However, they are performed only once at the beginning of the function.

The comparison of the input string with its reverse, input_string == input_string[::-1], is the primary operation affecting the time complexity. It involves iterating through the string, comparing characters in a case-insensitive manner. This comparison also has a time complexity of O(n), where 'n' is the length of the input string.

The print statements, while they introduce some additional work, do not significantly impact the overall time complexity because they execute in constant time, O(1).

As a result, the dominant factor in the time complexity is the comparison of the input string with its reverse, which is O(n). Therefore, the overall time complexity of the code is O(n), making it a linear time algorithm.

"""