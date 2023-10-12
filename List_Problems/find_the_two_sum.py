# Given a list of integers and a target sum, find two numbers that add up to the target sum.

def two_sum(nums, target):
    complement_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in complement_map:
            return [complement_map[complement], i]

        complement_map[num] = i

    return None

def two_sum(nums, target):
    # Create a dictionary to store the complement of each number and its index.
    complement_map = {}

    # Loop through each element and its index in the 'nums' list.
    for i, num in enumerate(nums):
        # Calculate the complement, i.e., the value needed to reach the 'target'.
        complement = target - num

        # Check if the complement is present in the 'complement_map'.
        # If it is, we found a pair of numbers whose sum equals the 'target'.
        if complement in complement_map:
            # Return the indices of the two numbers that add up to the 'target'.
            return [complement_map[complement], i]

        # If the complement is not in the 'complement_map', store the current number
        # as the key and its index as the value in the dictionary.
        complement_map[num] = i

    # If no valid pair is found, return 'None' to indicate that no solution exists.
    return None

