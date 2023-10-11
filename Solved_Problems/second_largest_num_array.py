# Find the second largest number in the array.

def second_largest(arr):
    # Sort the array in descending order
    arr.sort(reverse=True)
    # The second largest number is the second element in the sorted array
    return arr[1]


# Example usage
print(second_largest([5, 7, 2, 8, 9, 1]))  # 8

"""

This method uses the sorted() function to sort the array, 
it uses a Timsort algorithm which is a hybrid of merge sort and insertion sort and has an average time complexity of O(n log n) and is also efficient for large datasets.

"""
