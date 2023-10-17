# Write a function to check if the first element of a list is equal to the last one,
# if it is print "Same" if not print "Not the same"
# if the list is empty print "Nothing to check, sorry"

def checking_first_last(list_to_check):
    if list_to_check == []:
        return "Nothing to check, sorry"
    elif list_to_check[0] == list_to_check[-1]:
        return "Same"
    elif list_to_check[0] != list_to_check[-1]:
        return "Not the same"


print(checking_first_last([1, 2, 3, 1]))
print(checking_first_last([1, 2, 3, 1, 2]))
print(checking_first_last([]))


"""

The time complexity of the code to check if the first and last elements of a list are the same is O(1), which is constant time. This is because the code only performs a fixed number of operations regardless of the size of the input list.

The code consists of a series of conditional statements that directly compare the first and last elements of the list, and these comparisons are performed in constant time.

Here's the breakdown:

The code checks if the input list is empty with if list_to_check == []. This check is performed in constant time, O(1).

The code checks if the first element is equal to the last element with if list_to_check[0] == list_to_check[-1]. This comparison is also performed in constant time, O(1).

Similarly, it checks if the first and last elements are not equal with if list_to_check[0] != list_to_check[-1]. This operation is also in constant time, O(1).

Since these comparisons and checks are all executed independently and take a fixed amount of time, the overall time complexity is O(1), indicating constant time.

"""