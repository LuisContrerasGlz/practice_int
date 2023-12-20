# Program to determine whether two strings are the anagram

"""

Definition:
An anagram is a word or phrase formed by rearranging the letters of another. For example, "listen" and "silent" are anagrams.

Objective:
Write a program to determine whether two given strings are anagrams.

Approach:

Character Count:

An anagram should have the same characters with the same frequency, but their order can be different.
Count the occurrences of each character in both strings.
Comparison:

Compare the character counts obtained for both strings.
If the character counts are the same, the strings are anagrams; otherwise, they are not.
Example:
Let's take an example:

String 1: "listen"
String 2: "silent"
Count of characters:

String 1: {'l': 1, 'i': 1, 's': 1, 't': 1, 'e': 1, 'n': 1}
String 2: {'s': 1, 'i': 1, 'l': 1, 'e': 1, 'n': 1, 't': 1}
Since the character counts match, the strings "listen" and "silent" are anagrams.

Note:

Make sure to handle uppercase and lowercase characters uniformly.
Remove spaces and consider only letters.

"""