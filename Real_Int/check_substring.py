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
    for i in range(len(input_string)):
        # Comprobamos si el carácter actual ya está en la subcadena actual
        if (input_string[i] in current_substring):
            # Si el carácter está duplicado, comparamos longitudes y actualizamos si es necesario
            if (len(current_substring) > len(longest_substring)):
                longest_substring = current_substring
            # Restablecemos la subcadena actual para comenzar una nueva
            current_substring = input_string[i]
        else:
            # Si el carácter es único, lo agregamos a la subcadena actual
            current_substring = current_substring + input_string[i]
    
    # Comprobamos una vez más al final para asegurarnos de que la última subcadena sea la más larga si es el caso
    if (len(current_substring) > len(longest_substring)):
        longest_substring = current_substring

    # Devolvemos la subcadena más larga con caracteres únicos encontrada
    return longest_substring

# Ejemplo de uso
input_string = "abcaabcde"
result = find_longest_unique_substring(input_string)
print(result)  # Debe imprimir "abcde"
