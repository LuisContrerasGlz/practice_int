# Given two strings, find their union.

def union_of_strings(s1, s2):
    # Convert the strings to sets
    set1 = set(s1)
    set2 = set(s2)
    # Find the union of the sets
    union_set = set1.union(set2)
    # Convert the union set back to a string
    return "".join(union_set)


# Example usage
print(union_of_strings("Hello", "World"))  # "HeloWrd"
