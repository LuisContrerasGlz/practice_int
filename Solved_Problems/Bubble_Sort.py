# Bubble sort has a complexity of O(n**2)

def bubble_sort_while(arr):
    # Indexing for the len -1 because we cant compare the last one since there is nothing after
    indexing_length = len(arr) - 1
    # Var which will takes us out from the loop when it is sorted
    sorted = False

    # We enter this while with the not sorted
    while not sorted:
        # We turn it to true so it takes us out when the array is sorted
        sorted = True
        # Looping and swaping the values when necessary
        for i in range(0, indexing_length):
            if arr[i] > arr[i+1]:
                # Moving sorted to false which happens only when it is not sorted yet so it does the while again
                sorted = False
                arr[i], arr[i+1] = arr[i+1], arr[i]
    # We print the sorted array
    return arr


# Example usage
arr = [5, 1, 4, 2, 8]
arr2 = [5, 1, 4, 2, 8, 3, 10, 13, 9, 23, 48, 100]
sorted_arr = bubble_sort_while(arr)
print(sorted_arr)  # [1, 2, 4, 5, 8]
sorted_arr2 = bubble_sort_while(arr2)
print(sorted_arr2)  # [1, 2, 4, 5, 8]
