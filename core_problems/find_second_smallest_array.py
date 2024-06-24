# Find Second Smallest Number 

def second_smallest_elem_array(list_to_check):
    # Check if the list has at least two elements
    if len(list_to_check) < 2:
        return None  
    
    # Sort the list in ascending order
    sorted_list = sorted(list_to_check)
    
    # Find the second smallest element
    return sorted_list[1]  # Use index 1 to get the second smallest element
