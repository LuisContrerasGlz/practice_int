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
