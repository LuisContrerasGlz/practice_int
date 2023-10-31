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