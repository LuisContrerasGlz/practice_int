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
    # We keep track of the position of the sequence with the variable seqIdx
    seqIdx = 0
    # We traverse the array in this for loop
    for value in array:
        # If the len of the sequence is equal to the value of seqIdx which will be increased each time there is a match equals the len of the sequence
        # That means we found all the values in the sequence contained in the array in the same order so we break
        if seqIdx == len(sequence):
            break
        # If the value at the position of sequence is in the current value of the array we increase the value of seqIdx by 1 so we move on to the next value in the sequence
        if sequence[seqIdx] == value:
            seqIdx += 1
    # Then we just return True or False depending if the positions were completed and equals to the sequence, meaning that all the elements in the sequence were in the array in that order
    return seqIdx == len(sequence)
