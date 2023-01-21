

# Using O(n2) with 2 for loops
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(len(nums)):
            if (i == j):
                continue
            else:
                if (nums[i] + nums[j] == target):
                    return [i, j]


print(twoSum([1, 2, 3, 4, 5, 6,], 6))

# Using a HashMap/Dictionary for the solution


def twoSumDict(nums2, target2):
    hashmap = {}
    for i in range(len(nums2)):
        diff = target2 - nums2[i]
        print(diff)
        if diff in hashmap:
            return [hashmap[diff], i]
        else:
            hashmap[nums2[i]] = i
            print(hashmap)


print(twoSumDict([1, 7, 9, 4, 5, 6,], 6))
