# Find two numbers in an array that add up to a specific target sum

def two_sum_array(origin_list, target):
    for i in range(len(origin_list)):
        for j in range(i+1,len(origin_list)):
            if origin_list[i] + origin_list[j] == target:
                return [origin_list[i], origin_list[j]]
            

print(two_sum_array([2,3,5,1], 4))

"""

While this code is correct and will find a valid pair of numbers that add up to the target, it has a time complexity of O(n^2), which means it will become inefficient for large input lists. 
The nested loops result in a lot of unnecessary comparisons, especially when there's no match.

"""
        