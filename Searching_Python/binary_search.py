"""

Binary Search:

Binary search is a more efficient algorithm that works on sorted lists.
It repeatedly divides the search interval in half until the target element is found.
Time complexity: O(log n) in the worst case, where 'n' is the number of elements in the list.

"""

def binary_search(arr, target):

    low = 0, 
    high= len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
