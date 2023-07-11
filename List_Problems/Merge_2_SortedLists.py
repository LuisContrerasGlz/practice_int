# Given two sorted lists, merge them into a single sorted list.

# Use the merge() function from the heapq module.
"""
heapq.merge() takes 2 sorted lists as input and returns an iterator that produces items from both lists in sorted order. 
By converting the iterator to a list using list(), we obtain the merged sorted list.
"""

import heapq

def merge_sorted_lists(list1, list2):
    return list(heapq.merge(list1, list2))

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged_list = merge_sorted_lists(list1, list2)
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
