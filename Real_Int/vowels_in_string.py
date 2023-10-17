"""

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

"""

def count_vowels(input_string):
    num_vowels = 0
    vowels = ["a", "e", "i", "o", "u"]

    for char in input_string:
        if char in vowels:
            num_vowels =  num_vowels +1

    return num_vowels


s = "ynbozunejaomfsosfyuqoqa"
num_vowels = count_vowels(s)
print("Number of vowels: " + str(num_vowels))

"""

The time complexity of the code to count the number of vowels in a string is O(n), where 'n' is the length of the input string.

Here's the breakdown of the time complexity:

The code uses a for loop to iterate over each character in the input string. This loop contributes O(n) time complexity, where 'n' is the length of the input string.

Inside the loop, it checks if the current character is in the list of vowels. The char in vowels operation has a time complexity of O(k), where 'k' is the number of elements in the vowels list (which is a constant 5 in this case). This check is performed within the loop, so it adds up to O(n) for all characters in the input string.

As a result, the dominant factor in the time complexity is the loop that iterates through the characters in the input string, making the overall time complexity O(n), which is linear with respect to the size of the input string.

"""

