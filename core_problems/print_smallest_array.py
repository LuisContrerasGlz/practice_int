# Print the smallest element in an array

def print_smallest_element(arr):
    # Check if the array is empty
    if not arr:
        print("Array is empty")
        return
    
    # Initialize the smallest element with the first element of the array
    smallest = arr[0]
    
    # Iterate through the array to find the smallest element
    for num in arr:
        if num < smallest:
            smallest = num
    
    # Print the smallest element
    print("The smallest element in the array is:", smallest)
