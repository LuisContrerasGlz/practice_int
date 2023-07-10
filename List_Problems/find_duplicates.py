# Find the duplicates in a list and print them 

def find_duplicates(lst):
    frequency = {}
    duplicates = []

    # Count the frequency of each element in the list
    for num in lst:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1

    # Find the duplicates
    for num, count in frequency.items():
        if count > 1:
            duplicates.append(num)

    return duplicates

# Example usage
my_list = [1, 2, 3, 4, 4, 5, 2, 6, 7, 6]
duplicate_nums = find_duplicates(my_list)
print(duplicate_nums)
