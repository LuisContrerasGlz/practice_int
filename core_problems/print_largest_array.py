# Print the largest element in an array 

def largest_elem_array(list_to_check):
    sorted_list = sorted(list_to_check)
    return sorted_list[-1]


largest_elem_array([2,4,6,7,8,1,0])

# Using for

def largest_elem_array(list_to_check):
    # Initialize the first element as the largest
    largest = list_to_check[0]
    
    # Iterate through each element in the list
    for elem in list_to_check:
        # Update the largest if the current element is greater
        if elem > largest:
            largest = elem
    
    # Return the largest element
    return largest

print(largest_elem_array([2, 4, 6, 7, 8, 1, 0]))  # Output: 8
