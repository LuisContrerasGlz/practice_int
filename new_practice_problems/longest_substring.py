# Program to Find Longest Substring Without Repeating Characters


"""

Approach:

Sliding Window Technique:

Use a sliding window approach to traverse the string.
Character Set:

Maintain a set to keep track of unique characters within the current window.
Adjust Window:

Adjust the window by moving the right boundary to expand the substring or the left boundary to shrink it.
Result:

Keep track of the length of the longest substring without repeating characters.
Example:
Let's take an example:

Input String: "abcabcbb"
Find the longest substring without repeating characters:

Longest Substring: "abc"
Note:

The sliding window technique is efficient for this problem.
Handle situations where the input string may be empty.


"""