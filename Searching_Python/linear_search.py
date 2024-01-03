"""

Linear Search:

Linear search is a simple and straightforward method that iterates through each element in a sequence until the desired element is found.
It is suitable for unsorted lists.
Time complexity: O(n) in the worst case, where 'n' is the number of elements in the list.

"""

def linear_search(arr, target):
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1
