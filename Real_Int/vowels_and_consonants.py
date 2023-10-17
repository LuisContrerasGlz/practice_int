# Given a string find the number of vowels and consonants

def count_vowels_consonants(s):

    vowels = "aeiouAEIOU"
    vowels_count = 0
    consonants_count = 0

    for char in s:
        if char.isalpha():
            if char in vowels:
                vowels_count += 1
            elif char.isupper() or char.islower():
                consonants_count += 1
    return vowels_count, consonants_count


print(count_vowels_consonants("Hello World!@#987"))  # (3, 7)


"""

The time complexity of the code to count the number of vowels and consonants in a string is O(n), where 'n' is the length of the input string.

Here's the breakdown of the time complexity:

The code uses a for loop to iterate over each character in the input string. This loop contributes O(n) time complexity, where 'n' is the length of the input string.

Inside the loop, it checks if the current character is an alphabetic character using char.isalpha(). This check is performed in constant time (O(1)).

Within the alphabetic character check, it checks if the character is a vowel using char in vowels. The char in vowels operation has a time complexity of O(k), where 'k' is the number of characters in the vowels string (which is a constant 10 in this case).

It also checks if the character is an uppercase or lowercase letter using char.isupper() and char.islower(), both of which are constant-time operations.

As a result, the dominant factor in the time complexity is still the loop that iterates through the characters in the input string, making the overall time complexity O(n), which is linear with respect to the size of the input string.

"""