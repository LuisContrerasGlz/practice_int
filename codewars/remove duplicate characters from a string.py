# Program to remove duplicate characters from a string

def remove_duplicates(input_str):
    # Convert the string to a set to eliminate duplicates
    unique_chars = set(input_str)
    # Join the unique characters back into a string
    result = ''.join(unique_chars)
    
    return result

# Example usage
input_string = "hello"
print(remove_duplicates(input_string))  # Output: "helo"
