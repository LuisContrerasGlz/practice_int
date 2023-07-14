# Given a list of integers and a target sum, find two numbers that add up to the target sum.

def two_sum(nums, target):
    complement_map = {}

    for i, num in enumerate(nums):
        complement = target - num

        if complement in complement_map:
            return [complement_map[complement], i]

        complement_map[num] = i

    return None
