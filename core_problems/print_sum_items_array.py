# Print the sum of all the items of the array 

def sum_items(items):
    sum_of_items = 0
    for i in items:
        sum_of_items = sum_of_items + i
    
    return sum_of_items

print(sum_items([2,2,2,2]))