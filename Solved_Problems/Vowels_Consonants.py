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


# Example usage
print(count_vowels_consonants("Hello World!@#987"))  # (3, 7)
