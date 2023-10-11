# Given a string, remove the consecutively repeated characters.
# For example - aabbbcabcbb to cabc.

def remove_consecutive_duplicates(string_from_user):
    # Initialize an empty string to store the result
    result = ""
    # Iterate through the string
    for i in range(len(string_from_user)):
        # If the current character is not the same as the previous character,
        # add it to the result string
        if i == 0 or string_from_user[i] != string_from_user[i-1]:
            result += string_from_user[i]
    return result


# Example usage
print(remove_consecutive_duplicates("aabbbcabcbb"))  # "cabc"
