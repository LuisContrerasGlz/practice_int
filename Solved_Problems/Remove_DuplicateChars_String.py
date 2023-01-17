# Remove all the duplicate characters present in the given string.


# Unsorted

def remove_duplicates(s):
    # Convert the string to a set, which automatically removes duplicates
    # Then join the set back into a string
    return ''.join(set(s))


# Example usage
print(remove_duplicates("hello world"))  # "helo wrd"

# Sorted


def remove_duplicates2(string):
    return "".join(sorted(set(string), key=string.index))
