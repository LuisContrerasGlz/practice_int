def first_letter(str_check):
    # Split the input string into words
    words_str = str_check.split()
    
    # Create a list to hold the first letters of each word
    first_letters = []
    
    # Iterate through each word in the split string
    for word in words_str:
        # Append the first letter of each word to the list
        first_letters.append(word[0])
    
    # Return the list of first letters
    return first_letters

# Example usage:
print(first_letter("Hey This is a test"))  # Output: ['H', 'T', 'i', 'a', 't']
