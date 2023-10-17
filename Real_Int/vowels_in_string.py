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

