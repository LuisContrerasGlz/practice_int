# Program to count occurrences of a word in string

"""

Approach:

Tokenization:

Split the input string into individual words. This involves separating the string based on spaces or other delimiters.
Count Occurrences:

Traverse through the words obtained after tokenization.
For each word, compare it with the target word.
If a match is found, increment a counter.
Result:

The counter value represents the number of occurrences of the target word.
Example:
Let's take an example:

Input String: "This is a sample string. This string is for an example."
Count occurrences of the word "string":

Result: 2

Note:

Handle variations in case sensitivity (e.g., "String" vs. "string").
Consider whether you want to count partial matches or only complete word matches.

"""