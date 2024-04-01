# Removing duplicate characters from a list

def remove_duplicates_from_list(input_list):
    # Convert the list to a set to eliminate duplicates
    unique_elements = set(input_list)
    # Convert the set back to a list
    result = list(unique_elements)
    
    return result

# Example usage
input_list = [1, 2, 3, 4, 2, 3, 5]
print(remove_duplicates_from_list(input_list))  # Output: [1, 2, 3, 4, 5]
