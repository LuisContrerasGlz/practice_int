# Find Second Largest Number in an Array 

def second_largest_elem_array(list_to_check):
    # Check if the list has at least two elements
    if len(list_to_check) < 2:
        return None  
    
    # Sort the list in ascending order
    sorted_list = sorted(list_to_check)
    
    # Find the second largest element
    return sorted_list[-2]


print(second_largest_elem_array([2, 4, 6, 7, 8, 1, 0]))  # Output: 7
print(second_largest_elem_array([8, 8, 8, 8]))  # Output: 8
print(second_largest_elem_array([3, 3, 3]))  # Output: 3
print(second_largest_elem_array([8]))  # Output: None (or handle appropriately)
