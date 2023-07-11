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

# Implementing a custom merging algorithm:
"""
we iterate through both lists using two pointers (i and j). 
At each iteration, we compare the current elements from both lists and append the smaller one to the merged_list. 
We increment the corresponding pointer and continue until we reach the end of either list. 
Finally, we append any remaining elements from the lists to the merged_list.
"""

def merge_sorted_lists(list1, list2):
    merged_list = []
    i = j = 0

    while i < len(list1) and j < len(list2):
        if list1[i] <= list2[j]:
            merged_list.append(list1[i])
            i += 1
        else:
            merged_list.append(list2[j])
            j += 1

    # Append any remaining elements from the lists
    merged_list.extend(list1[i:])
    merged_list.extend(list2[j:])

    return merged_list

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged_list = merge_sorted_lists(list1, list2)
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
