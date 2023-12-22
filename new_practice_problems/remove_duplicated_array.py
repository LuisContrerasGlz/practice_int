# Remove duplicates from Array

"""

Approach:

Initialize Data Structure:

Use a data structure, such as a set, to keep track of unique elements encountered.
Iterate Through Array:

Traverse each element in the array.
Remove Duplicates:

For each element, check whether it has been encountered before.
If it's a new element, add it to the set.
If it's a duplicate, skip it.
Result:

The elements in the set represent the array with duplicates removed.
Example:
Let's take an example:

Array: [3, 5, 7, 3, 9, 7, 5]
Remove duplicates:

Resulting Array: [3, 5, 7, 9]
Note:

The order of elements may or may not be preserved, depending on the specific requirements.
The time complexity of this solution is O(n), where n is the total number of elements in the array.

"""