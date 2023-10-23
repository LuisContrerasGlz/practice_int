# Given a string s, find the length of the longest substring without repeating characters.

"""


Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


"""

def find_longest_unique_substring(input_string):
    
    # Variables para rastrear la subcadena actual y la subcadena más larga

    current_substring = ""  # Subcadena actual que se está construyendo
    longest_substring = ""  # Subcadena más larga encontrada hasta el momento

    # Iteramos a través de la cadena de entrada
    for i in input_string:
        # Comprobamos si el carácter actual ya está en la subcadena actual
        if i in current_substring:
            # Si el carácter está duplicado, comparamos longitudes y actualizamos si es necesario
            if (len(current_substring) > len(longest_substring)):
                longest_substring = current_substring
            # Restablecemos la subcadena actual para comenzar una nueva
            current_substring = i
        else:
            # Si el carácter es único, lo agregamos a la subcadena actual
            current_substring = current_substring + i
    
    # Comprobamos una vez más al final para asegurarnos de que la última subcadena sea la más larga si es el caso
    if (len(current_substring) > len(longest_substring)):
        longest_substring = current_substring

    # Devolvemos la subcadena más larga con caracteres únicos encontrada
    return longest_substring


input_string = "abcaabcde"
result = find_longest_unique_substring(input_string)
print(result)  # Debe imprimir "abcde"


"""

The time complexity of the provided code is O(n), where 'n' is the length of the input string input_string.

Here's the breakdown:

The code uses a for loop to iterate over each character in the input string. This loop contributes O(n) time complexity.

Inside the loop, it checks if the current character is in the current_substring. Checking whether a character is in a string can be done in O(m) time, where 'm' is the length of the string being checked. In the worst case, 'm' is the length of the current_substring, but because each character is checked at most once, the total time spent on these checks across all iterations of the loop is still O(n).

The code also compares the length of the current_substring with the length of the longest_substring and updates longest_substring when needed. These operations are performed in constant time, O(1), within the loop.

Finally, the code checks once more at the end to ensure that the current_substring is the longest. This check runs in constant time, O(1).

As a result, the total time complexity is O(n), making the code efficient for finding the longest substring with unique characters in the input string.


"""