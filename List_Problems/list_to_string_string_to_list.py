# Convert a List to a String
# You can join the elements of a list into a single string using the join() method

my_list = ['Hello', 'world', '!', 'Python']
list_as_string = ' '.join(my_list)
print(list_as_string)

my_list = ['apple', 'banana', 'orange']
list_as_string = ','.join(my_list)
print(list_as_string)


# Convert a String into a list 
# You can split a string into a list of substrings using the split() method.
# By default, it splits the string at whitespace characters (spaces, tabs, and newlines) and returns a list of substrings.

my_string = "Hello world! Python"
string_as_list = my_string.split()
print(string_as_list)

my_string = "apple,banana,orange"
string_as_list = my_string.split(',')
print(string_as_list)