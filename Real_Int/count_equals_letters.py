# Count the equal letters from a string/text using a dictionary

def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
        result[letter] += 1
    return result


print(count_letters("aaaabbbccd"))

"""


The time complexity of the code to count the occurrences of letters in a text is O(n), where 'n' is the length of the input text.

Here's the breakdown of the time complexity:

The code uses a for loop to iterate over each character (letter) in the input text. This loop contributes O(n) time complexity, where 'n' is the length of the input text.

Inside the loop, it checks if the current letter is already in the result dictionary. The dictionary lookup (letter not in result) typically has an average-case time complexity of O(1) because dictionary keys are implemented as hash tables. However, in the worst case, where there are collisions, it can be O(n), but this is rare in practice.

After checking for the presence of the letter in the dictionary, it increments the count for that letter, which is also an O(1) operation within the loop.

As a result, the dominant factor in the time complexity is the loop that iterates through the characters in the input text, making the overall time complexity O(n), which is linear with respect to the size of the input text.

"""