# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

# Using a set O(n)
def containsDuplicate(nums):
    return len(set(nums)) != len(nums)


print(containsDuplicate([1, 1, 2, 3, 4, 5, 6]))

# Using a HashMap/Dictionary


def contains_duplicate(nums2):
    d = {}
    for num in nums2:
        if num in d:
            return True
        else:
            d[num] = 1
    return False


print(contains_duplicate([1, 1, 2, 3, 4, 5, 6]))
