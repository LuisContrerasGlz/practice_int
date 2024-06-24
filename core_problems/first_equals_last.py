# Write a function to check if the first element of a list is equal to the last one,
# if it is print "Same" if not print "Not the same"
# if the list is empty print "Nothing to check, sorry"

def check_first_last_equality(elements_list):

    if len(elements_list) == 0:
        print("Nothing to check, sorry")
    elif elements_list[0] == elements_list[-1]:
        print("Same")
    else:
        print("Not the Same")

check_first_last_equality([1,2,3,4,1])