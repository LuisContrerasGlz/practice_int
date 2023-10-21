"""

Write a program that prints the numbers from 1 to 100. 
But for multiples of three print “Fizz” instead of the number and for the multiples of five print “Buzz”. 
For numbers which are multiples of both three and five print “FizzBuzz”.


"""

for i in range(1,101):
    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")
    elif i % 3 == 0:
        print("Fizz")
    elif i % 5 == 0:
        print("Buzz")
    else:
        print(i)

"""

The time complexity, or Big O notation, of the provided "FizzBuzz" solution is O(n), where "n" is the range of numbers from 1 to 100 (inclusive). In this case, "n" is 100.

Here's why the solution has a linear time complexity of O(n):

The code iterates through all the numbers from 1 to 100 exactly once using a loop (for i in range(1, 101)).
For each number, there are a constant number of operations performed to check if it's a multiple of 3, a multiple of 5, or both. These operations are constant time, so they don't significantly affect the overall time complexity.
Since the number of iterations in the loop is directly proportional to the input range (100 in this case), the time complexity is linear, O(n).

In summary, this "FizzBuzz" solution is an efficient and straightforward algorithm with a time complexity of O(n), making it suitable for the given problem.

"""