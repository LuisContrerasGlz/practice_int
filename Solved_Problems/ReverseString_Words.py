# Given a string, print the string by reversing its words.

def reverse_words_in_string(s):
    words = s.split()
    return " ".join(words[::-1])


print(reverse_words_in_string("Hello How Are You"))
