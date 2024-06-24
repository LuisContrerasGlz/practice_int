from collections import Counter

# Find the frequency of each element in the array 

def find_frequencies(array):
    frequency_dict = {}
    
    for element in array:
        # Check if the element is already in the dictionary.
        if element in frequency_dict:
            # Increment the count of the element if it is already in the dictionary.
            frequency_dict[element] += 1
        # Initializes the count of the element to 1 if it is not in the dictionary.
        else:
            frequency_dict[element] = 1
            
    # Iterate through the dictionary items and print each element(key) and its corresponding frequency(value).        
    for element, frequency in frequency_dict.items():
        print(f"Element: {element}, Frequency: {frequency}")

array = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
find_frequencies(array)

# Using collections.Counter

from collections import Counter


def find_frequencies(array):
    # Create a Counter object to count the frequency of each element in the array
    frequency_dict = Counter(array)
    
    # Iterate through the items of the Counter object
    for element, frequency in frequency_dict.items():
        # Print each element and its frequency
        print(f"Element: {element}, Frequency: {frequency}")

array = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
find_frequencies(array)

