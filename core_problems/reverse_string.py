# Reverse a string 

def reverse_str(str_reverse):
    return str_reverse[::-1]

def reverse_str2(str_reverse2):
    reversed_str = ""

    for i in str_reverse2:
        reversed_str = i + reversed_str

    return reversed_str