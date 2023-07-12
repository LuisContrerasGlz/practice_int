# Given two lists, find the intersection (common elements) between them.

def find_intersection(list1, list2):
    """
    We first convert both lists to sets using the set() constructor. 
    Sets are unordered collections that only contain unique elements. 
    By converting the lists to sets, we eliminate any duplicate elements.

    We then use the intersection() method of sets to find the common elements between the two sets (set1 and set2). 
    The intersection() method returns a new set that contains only the elements present in both sets.
    Finally, we convert the resulting set back to a list using the list() constructor to obtain the intersection as a list.

    Overall time complexity of O(N), where N is the size of the largest list.

    """
    set1 = set(list1)
    set2 = set(list2)
    intersection = set1.intersection(set2)
    return list(intersection)

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection_list = find_intersection(list1, list2)
print(intersection_list)  # Output: [4, 5]
