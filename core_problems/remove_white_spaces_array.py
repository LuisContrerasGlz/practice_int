# From an Array remove all the white spaces


def remove_whitespaces(array):
    new_lst = []
    for element in array:
        no_space = element.replace(" ", "")
        new_lst.append(no_space)
    
    return new_lst
    
input_array = ["hello world", "  example  ", "remove whitespaces"]
cleaned_array = remove_whitespaces(input_array)
print(cleaned_array)