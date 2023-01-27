"""

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'.

"""

s = "ynbozunejaomfsosfyuqoqa"
num_vowels = 0

for char in s:
    if char in ["a", "e", "i", "o", "u"]:
        num_vowels += 1

print("Number of vowels: " + str(num_vowels))
