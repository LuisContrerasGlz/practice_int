# Find longest common prefix in given array of strings and return none if no prefix matches Input = {"flower", "flow", "fly"} Output = fl


"""

Approach:

Initialize Prefix:

Start with an empty string as the initial common prefix.
Iterate Through Characters:

For each position (index) in the strings, compare the characters at that position for all strings.
If the characters are the same, add the character to the common prefix.
If the characters are different, stop the iteration.
Result:

The result is the longest common prefix obtained during the iteration.
Handle No Common Prefix:

If no common prefix is found (i.e., the iteration completes without adding any characters to the prefix), return "None" or an appropriate indicator.
Example:
Let's take an example:

Input Strings: {"flower", "flow", "fly"}
Find the longest common prefix:

Common Prefix: "fl"
Note:

Handle situations where the array is empty.
The common prefix is determined character by character until a mismatch is encountered.

"""
