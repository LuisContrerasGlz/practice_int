import re

# In a string program to count the number of words in a string 

def num_of_words(sentence):
    list_of_words = sentence.split(" ")
    num_of_words = len(list_of_words)
    print(f"The number of words on this string ({sentence}) is {num_of_words}")

num_of_words("Hello this is a test")

# Using a regex to check space and comma

import re


def count_words(sentence):
    # Split by any whitespace or comma
    list_of_words = re.split(r'[,\s]+', sentence.strip())
    num_words = len([word for word in list_of_words if word])  # Filter out any empty strings
    print(f"The number of words in this string ('{sentence}') is {num_words}")
    return num_words

# Example usage
count_words("Hello, this is a test")
count_words("Hello, this is a test, with commas, and spaces")


