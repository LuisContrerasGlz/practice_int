"""

The code opens the file "my_information.txt" in write mode ('w') with the UTF-8 encoding.
If the file does not exist, it will be created. 
The with statement is used, ensuring that the file is properly closed after writing.

"""


with open("my_information.txt",'w',encoding=  'utf-8') as my_file:
    """

    Here, three lines of information are written to the file: 
    Tom Hardy's name, his profession, and the fact that he is active in charity work.

    """
    my_file.write("Name is Tom Hardy.\n")
    my_file.write("I am an English actor and a producer.\n")
    my_file.write("I am active in charity work.\n")

"""

Next, the code opens the same file "my_information.txt" in read mode ('r') with UTF-8 encoding. The with statement is used again.

a. print(my_file.readline()): This line reads the first line of the file and prints it. In this case, it will print "Name is Tom Hardy." and move the file pointer to the beginning of the next line.

b. my_file.seek(0, 0): This line moves the file pointer to the beginning of the file (offset 0 from the beginning).

c. print(my_file.readlines()): This line reads all the remaining lines in the file and prints them as a list. In this case, it will print the two remaining lines: "I am an English actor and a producer." and "I am active in charity work."

So, the overall functionality of the code is to write information about Tom Hardy to a file and then read and print that information from the same file.

"""

with open("my_information.txt",'r',encoding='utf-8') as my_file:
    print(my_file.readline())
    my_file.seek(0, 0)
    print(my_file.readlines())


