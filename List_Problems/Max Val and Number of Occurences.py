"""
Given an array of integers, return the maximum value and its number of occurences.
Your algorithm should run in O(n) time and use O(1) space.
"""


def maxValNumOfOccurrences(nums):
    max_value, count = nums[0], 0
    for value in nums:
        if value > max_value:
            max_value, count = value, 1
        elif value == max_value:
            count += 1
    return [max_value, count]


print(maxValNumOfOccurrences([2, 7, 11, 8, 11, 8, 3, 11]))