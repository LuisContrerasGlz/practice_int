# Count the number of same characters in a string  

def count_chars(input_string):
    num_count_chars = {}
    for i in input_string:
        if i not in num_count_chars:
            num_count_chars[i] = 1
        else:
            num_count_chars[i] += 1
    return num_count_chars

print(count_chars("hhheeellloooo"))


"""

The time complexity of the provided code is O(n), where "n" is the length of the input_string.

Here's why the code has a linear time complexity of O(n):

The code iterates through each character in the input_string exactly once. 
In the worst case, it visits every character in the string.
For each character, it performs dictionary operations (checking if a key exists and either adding a new key or incrementing an existing key).
Since the number of iterations in the loop is directly proportional to the length of the input_string, the time required to execute the entire loop increases linearly with the input size. 
Therefore, the overall time complexity of this code is O(n). It's an efficient way to count character occurrences in a string.


"""
