"""

Look through nums and find 2 values that add up to equal the tarjet value
Return their indices

"""

# O(n) Time and Space


def twoNumberSum(array, targetSum):
    # Declaring empty diccionary
    nums = {}
    # looping the array and working on the logic
    for num in array:
        # Calculating the number that would need to be in the dicctionary to make the sum equal to targetSum
        potentialMatch = targetSum - num
        # We check if the potentialMatch is in the dictionary, if it is then we return it plus nums since those 2 would make the targetSum
        if potentialMatch in nums:
            return [potentialMatch, num]
        # If the potentialMatch is not in the nums dicctionary we add it to the dicctionary by using the nums[num] = 1
        else:
            nums[num] = 1
    # If nothing was found to sum, we return an empty dicctionary
    return []
