# Remove Leading zeros from a list

def remove_leading_zeros(nums):
    # Edge case: if the list is empty, return an empty list
    if not nums:
        return []
    
    # Find the index of the first non-zero element
    first_non_zero_index = 0
    while first_non_zero_index < len(nums) and nums[first_non_zero_index] == 0:
        first_non_zero_index += 1
    
    # Return the sublist from the first non-zero element to the end
    return nums[first_non_zero_index:]