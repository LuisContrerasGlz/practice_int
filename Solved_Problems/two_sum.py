"""

Look through nums and find 2 values that add up to equal the tarjet value
Return their indices

"""

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

"""

Complexity Analysis

Time complexity: O(n2) 

For each element, we try to find its complement by looping through the rest of the array which takes O(n) time. 
Therefore, the time complexity is O(n2)O(n^2)O(n 

Space complexity: O(1). The space required does not depend on the size of the input array, so only constant space is used.

"""

# Using a HashMap/Dictionary for the solution


def twoSumDict(nums2, target2):
    hashmap = {}
    for i in range(len(nums2)):
        diff = target2 - nums2[i]
        print(diff)
        if diff in hashmap:
            return [i, hashmap[diff]]
        else:
            hashmap[nums2[i]] = i
            print(hashmap)


print(twoSumDict([1, 7, 9, 4, 5, 6,], 6))

"""

Complexity Analysis

Time complexity: O(n). We traverse the list containing nnn elements only once. Each lookup in the table costs only O(1) time.

Space complexity: O(n). The extra space required depends on the number of items stored in the hash table, which stores at most nnn elements.


"""
