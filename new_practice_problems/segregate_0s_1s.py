# Program to segregate 0s and 1s in given array. Input = {1,0,1,1,0,1,1,0,0} Output = {0,0,0,0,1,1,1,1,1}

"""

Approach:

Initialize Pointers:

Use two pointers, one for the left (start) and one for the right (end) of the array.
Traverse and Swap:

Move the left pointer from the start until a 1 is encountered.
Move the right pointer from the end until a 0 is encountered.
Swap the elements at the left and right pointers.
Result:

Continue this process until the left pointer is greater than or equal to the right pointer.
The array is now segregated with all 0s before 1s.
Example:
Let's take an example:

Input Array: [1, 0, 1, 1, 0, 1, 1, 0, 0]
Segregate 0s and 1s:

Resulting Array: [0, 0, 0, 0, 1, 1, 1, 1, 1]

Note:

This is known as the Dutch National Flag problem.


"""