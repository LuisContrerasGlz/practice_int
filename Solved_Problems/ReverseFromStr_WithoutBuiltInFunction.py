# Given a sentence as a string,
# reverse each of the words without using inbuilt functions.

def reverse_words(sentence):
    # Split the sentence into a list of words
    words = sentence.split()
    # Iterate through the list of words
    for i in range(len(words)):
        # Reverse the order of the characters in each word
        words[i] = words[i][::-1]
    # Join the reversed words back into a sentence
    return " ".join(words)


# Example usage
print(reverse_words("Hello World"))  # "olleH dlroW"
