# In a given string containing 1s and 0s, find the number of 1s.

numbers_to_check = "11110001"
num_of_1s = 0

for i in range(len(numbers_to_check)):
    if numbers_to_check[i] == "1":
        num_of_1s += 1
print(num_of_1s)
