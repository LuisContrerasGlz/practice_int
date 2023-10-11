"""
Given an array of integers, return the maximum value and its number of occurences.
Your algorithm should run in O(n) time and use O(1) space.
"""


def maxValNumOfOccurrences(nums):
    # Initialize 'max_value' and 'count' variables to keep track of the maximum value and its occurrence count.
    max_value, count = nums[0], 0

    # Iterate through each 'value' in the 'nums' list.
    for value in nums:
        # Check if the current 'value' is greater than the current 'max_value'.
        if value > max_value:
            # If it is, update 'max_value' to the current 'value' and reset 'count' to 1.
            max_value, count = value, 1
        # If the current 'value' is equal to the current 'max_value'.
        elif value == max_value:
            # Increment 'count' by 1 since we encountered another occurrence of the 'max_value'.
    # After iterating through the entire list, return the 'max_value' and its occurrence 'count' as a list.
    return [max_value, count]



print(maxValNumOfOccurrences([2, 7, 11, 8, 11, 8, 3, 11]))