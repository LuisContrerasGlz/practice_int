"""

Given two non-empty arrays of integers, write a function that determines
whether the second array is a subsequence of the first one.

A subsequence of an array is a set of numbers that aren't necessarily adjacent
  in the array but that are in the same order as they appear in the array. For
  instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4] 
  and so the numbers [2, 4]

"""

# Time = O(N) Space = O(1)
"""

Initialize a variable "seqIdx" to 0 to keep track of the current position in the "sequence".

Loop through each value in the "array".

If the "seqIdx" is equal to the length of the "sequence", it means we have found all the elements of the sequence, so the loop breaks.

If the current value in the "array" is equal to the value at the current position in the "sequence", we increment the "seqIdx" by 1 to move to the next position in the "sequence".

After the loop, if "seqIdx" is equal to the length of the "sequence", it means we have found all the elements of the sequence in the "array", and the function returns True. If not, it returns False.

"""


def isValidSubsequence(array, sequence):
    seqIdx = 0
    for value in array:
        if seqIdx == len(sequence):
            break
        if sequence[seqIdx] == value:
            seqIdx += 1
    return seqIdx == len(sequence)
