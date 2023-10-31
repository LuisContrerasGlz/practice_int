// In Java, method overloading allows a class to have more than one method with the same name if their parameter lists are different.

public class OverloadExample {
    public int add(int a, int b) {
        return a + b;
    }

    public int add(int a, int b, int c) {
        return a + b + c;
    }

    public static void main(String[] args) {
        OverloadExample overload = new OverloadExample();
        System.out.println(overload.add(2, 3));        // Output: 5
        System.out.println(overload.add(2, 3, 4));    // Output: 9
    }
}


// In this example, the add method is overloaded with two versions having different numbers of parameters. 
// Depending on the arguments passed, the appropriate method is called.

// In Java, method overriding occurs when a subclass provides a specific implementation of a method that is already provided by its superclass.

class Animal {
    public void makeSound() {
        System.out.println("Generic sound");
    }
}

class Dog extends Animal {
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }
}

public class OverrideExample {
    public static void main(String[] args) {
        Animal animal = new Animal();
        animal.makeSound();  // Output: Generic sound

        Animal dog = new Dog();
        dog.makeSound();     // Output: Bark 
    }
}



