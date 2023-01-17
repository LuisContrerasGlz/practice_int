"""

Given a list of filenames, we want to rename all the files with extension hpp to the extension h. 
To do this, we would like to generate a new list called newfilenames, consisting of the new filenames. 

"""

# Using list comprehension

filenames = ["program.c", "stdio.hpp",
             "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
newfilenames = [i.replace("hpp", "h") if i.endswith(
    "hpp") else i for i in filenames]

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]+

# Using for loop

filenames = ["program.c", "stdio.hpp",
             "sample.hpp", "a.out", "math.hpp", "hpp.out"]
# Generate newfilenames as a list containing the new filenames
# using as many lines of code as your chosen method requires.
# newfilenames = [i.replace("hpp","h") if i.endswith("hpp") else i for i in filenames]
newfilenames = filenames.copy()
for i in range(len(newfilenames)):
    if newfilenames[i].endswith("hpp"):
        newfilenames[i] = newfilenames[i].replace("hpp", "h")

print(newfilenames)
# Should be ["program.c", "stdio.h", "sample.h", "a.out", "math.h", "hpp.out"]
