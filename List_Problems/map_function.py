# Applying a function to each element of a list without map

li = [2,3,4,6,8,9,10,11]

def exp_2(x):
    return x ** 2

new_li = []
for i in li:
    new_li.append(exp_2(i))
print(new_li)


# Now with map function

print(list(map(exp_2,li)))

# Using a list comprehension for the same 

print([exp_2(i) for i in li])

# Only for even numbers

print([exp_2(i) for i in li if i %2 == 0])