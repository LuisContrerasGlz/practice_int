"""

In Python, method overriding is a concept used in inheritance. 
When a method in a child class has the same name and signature as a method in the parent class, 
it overrides the method in the parent class.


"""

class Animal:
    def make_sound(self):
        print("Generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Bark")

# Usage
animal = Animal()
animal.make_sound()  # Output: Some generic sound

dog = Dog()
dog.make_sound()  # Output: Bark


"""

In Python, overloading isn't directly supported as in languages like Java or C++. 
However, Python allows function overloading by default due to its dynamic nature. 
Functions can be defined in a way that they behave differently based on the number or types of arguments passed.

"""

class OverloadExample:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c

# Usage
overload = OverloadExample()
print(overload.add(2, 3))        # This would raise an error as Python does not support traditional method overloading.
print(overload.add(2, 3, 4))    # This will work as expected.
