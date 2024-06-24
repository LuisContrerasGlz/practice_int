# Program to check whether a string is a Palindrome  

def is_palindrome(str_to_check):
    # Remove spaces and convert to lowercase for a case-insensitive comparison
    normalized_str = str_to_check.replace(" ", "").lower()
    
    if normalized_str == normalized_str[::-1]:
        print("is palindrome")
    else:
        print("not palindrome")