# Making it a function

def rev_str_for(or_str2):
    rev_or_srt2 = ""
    for i in or_str2:
        rev_or_srt2 =  i + rev_or_srt2
    return rev_or_srt2

print(rev_str_for("Using a for loop now"))

#Palindrome check

def check_palindrome(str_to_check):
    print(str_to_check.lower())
    print(rev_str_for(str_to_check).lower())
    if str_to_check.lower() == rev_str_for(str_to_check).lower():
        print("Palindrome :v ")
    else:
        print("not palindrome :v")

check_palindrome("LOL")

# --------------------------------------------------------------------


# Using slice

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


input_str = "A man a plan a canal Panama"
result = is_palindrome(input_str)