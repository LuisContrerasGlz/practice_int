# How do you remove a given character from String?

s = "hello world"
char_to_remove = "l"
s = s.replace(char_to_remove, "")
print(s)  # "heo word"

# With function

def remove_char(origin_string, char_to_remove):
    origin_string = origin_string.replace(char_to_remove, "")
    return origin_string

print(remove_char("hello world", "l"))

"""

The time complexity of this code is O(n), where "n" is the length of the origin_string.

Here's why the code has a linear time complexity of O(n):

The str.replace() method operates by iterating through the characters of the origin_string to find and replace the specified character (char_to_remove).
The time it takes to perform this operation is directly proportional to the length of the origin_string (i.e., O(n)), where "n" is the number of characters in the string.
As the input size (the length of the origin_string) increases, the time required to execute the replace operation increases linearly. Therefore, the overall time complexity of this code is O(n).

"""