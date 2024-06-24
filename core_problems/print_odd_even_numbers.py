# In an Array print Odd and Even Numbers 

def odd_even(list_nums):
    odd_nums = []
    even_nums = []

    for i in list_nums:
        if i % 2 == 0:
            even_nums.append(i)
        else:
            odd_nums.append(i)
    
    return f"Odd numbers are {odd_nums}, even numbers are {even_nums}"

print(odd_even([2,3,4,5,6,7,8,10]))