# Given a string find the number of vowels and consonants

# O(n), where n is the length of the input string str_to_check.

vowels = ["a", "e", "i", "o", "u"]
consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l",
              "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]


def vowels_consonants(str_to_check):
    vowels_count = 0
    consonants_count = 0
    for i in str_to_check:
        if i.lower() in vowels:
            vowels_count += 1
        elif i.lower() in consonants:
            consonants_count += 1
    return f"the number of vowels is {vowels_count} and the number of consonants is {consonants_count}"


print(vowels_consonants("Hey whAts goiNg On"))
