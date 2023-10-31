# Writing to a file
with open('example.txt', 'w') as file:
    file.write("Hello, this is some text that will be written to the file.")

# Reading from the file
with open('example.txt', 'r') as file:
    content = file.read()
    print("Content of the file:")
    print(content)


"""

This Python code demonstrates writing a string to a file named example.txt and then reading the contents of that file. 

The open() function with the mode 'w' (write mode) is used to write content to the file.
The content is written using the write() method.
Subsequently, the file is opened again with the mode 'r' (read mode) to read its content.
The read() method reads the content and then it's printed to the console.

"""

# Writing to a file (appending)
with open('example.txt', 'a') as file:  # Use 'a' mode for append
    file.write("\nThis content will be appended to the file.")

# Reading from the file
with open('example.txt', 'r') as file:
    content = file.read()
    print("Content of the file:")
    print(content)


"""

The open() function uses 'a' mode for append, which will allow the content to be added to the end of the file without overwriting existing content.

A newline character (\n) is used to ensure the new content starts on a new line.

"""