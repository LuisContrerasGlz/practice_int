# Find two numbers in an array that add up to a specific target sum

def two_sums_index(origin_list, target):
    elements_dict  = {}

    for i, n in enumerate(origin_list):
        difference = target - n

        if difference in elements_dict:
            return [elements_dict[difference], i]
        elements_dict[n] = i


print(two_sums_index([2,3,5,1], 4))

"""

Time complexity of O(n), which is efficient, as it only requires a single pass through the list.

"""

def two_sums(origin_list, target):
    elements_dict  = {}

    for i, n in enumerate(origin_list):
        difference = target - n

        if difference in elements_dict:
            return origin_list[elements_dict[difference]], n
        elements_dict[n] = i


print(two_sums([2,3,5,1], 4))