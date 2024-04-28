# Assignment 1 Java

## Differentiate between JVM and JRE


The Java Virtual Machine (JVM) is like a computer that can run Java programs. It's like a computer that can understand and execute instructions written in a special language called Java Bytecode.

The Java Runtime Environment (JRE) is like a package that contains everything a Java program needs to run, including the JVM. It's like a package that includes everything a computer needs to run a program written in the special language Java Bytecode.

So, the JVM is like the computer and JRE is like the package containing everything the computer needs to run the program.


### Different types of operators in Java:

Java implements various types of operators:
- **Arithmetic Operators:** Used for basic mathematical operations like addition (+), subtraction (-), multiplication (*), division (/), and modulus (%).
- **Comparison Operators:** Used to compare two values and return a boolean result. Examples include equal to (==), not equal to (!=), greater than (>), less than (<), etc.
- **Logical Operators:** Used for logical operations such as AND (&&), OR (||), and NOT (!).
- **Assignment Operators:** Used to assign values to variables, like =, +=, -=, *=, /=, etc.
- **Bitwise Operators:** Perform operations at the bit-level. Examples include bitwise AND (&), bitwise OR (|), bitwise XOR (^), bitwise NOT (~), left shift (<<), right shift (>>), and unsigned right shift (>>>).

### Structure of a Java program:

```java
// Import statements if necessary

// Class definition
public class MyClass {
    // Main method (entry point of the program)
    public static void main(String[] args) {
        // Program logic goes here
        System.out.println("Hello, Java!"); // Example output statement
    }
}
```

- **Imports:** Optional, used to bring in classes or packages.
- **Class Definition:** Starts with `public class ClassName` where `ClassName` is the name of the class.
- **Main Method:** `public static void main(String[] args)` is the starting point of execution.
- **Program Logic:** Actual code goes inside the main method.

### Usage of arrays in Java:

Arrays in Java are used to store multiple values of the same type. They have a fixed size once initialized. Here's an example of declaring and using an array:

```java
public class ArrayExample {
    public static void main(String[] args) {
        // Declare and initialize an array of integers
        int[] numbers = {10, 20, 30, 40, 50};

        // Access elements of the array
        System.out.println("First element: " + numbers[0]); // Prints 10

        // Update an element
        numbers[2] = 35;

        // Iterate through the array
        for (int i = 0; i < numbers.length; i++) {
            System.out.println("Element at index " + i + ": " + numbers[i]);
        }
    }
}
```

In this example, `numbers` is an array of integers, and we demonstrate accessing elements, updating elements, and iterating through the array using a loop.




### Demonstrate the break and continue statements in Java:

**Break Statement Example:**
```java
public class BreakExample {
    public static void main(String[] args) {
        // Break statement example
        for (int i = 1; i <= 5; i++) {
            if (i == 3) {
                break; // Exit the loop when i equals 3
            }
            System.out.println("Value of i: " + i);
        }
    }
}
```

**Continue Statement Example:**
```java
public class ContinueExample {
    public static void main(String[] args) {
        // Continue statement example
        for (int i = 1; i <= 5; i++) {
            if (i == 3) {
                continue; // Skip this iteration when i equals 3
            }
            System.out.println("Value of i: " + i);
        }
    }
}
```

In the `BreakExample`, the loop breaks when `i` equals 3, while in the `ContinueExample`, the loop skips the iteration when `i` equals 3.

### Types of loops in Java:

Java has several types of loops:
1. **for loop:** Used for iterating over a range of values.
2. **while loop:** Executes a block of code as long as a condition is true.
3. **do-while loop:** Similar to a while loop but guarantees at least one execution of the block.
4. **enhanced for-each loop:** Simplifies iterating over arrays and collections.

### Modifiers in Java:

- **Default (Package-private):** When no access modifier is specified, it is accessible within the same package.
- **Public:** Accessible from any other class.
- **Private:** Accessible only within the same class.
- **Protected:** Accessible within the same package and subclasses outside the package.

```java
public class ModifierExample {
    int defaultVar; // Default access
    public int publicVar; // Public access
    private int privateVar; // Private access
    protected int protectedVar; // Protected access
}
```

### Final and Static keywords in Java:

- **Final:** Used to declare constants, prevent method overriding, or make a class immutable.
- **Static:** Used for class-level variables and methods, shared among all instances of the class.

```java
public class FinalStaticExample {
    public static final int CONSTANT_VALUE = 100; // Final constant
    public static int staticVar = 0; // Static variable

    public static void main(String[] args) {
        staticVar = 50; // Assigning a value to staticVar
        System.out.println("Constant value: " + CONSTANT_VALUE);
        System.out.println("Static variable value: " + staticVar);
    }
}
```

In this example, `CONSTANT_VALUE` is a final constant, and `staticVar` is a static variable that can be accessed without creating an instance of the class.

### i. Inheritance:
Inheritance allows a class (subclass/child class) to inherit properties and behaviors from another class (superclass/parent class). Here's an example:

```java
// Parent class (superclass)
class Animal {
    void eat() {
        System.out.println("Animal is eating");
    }
}

// Child class (subclass) inheriting from Animal
class Dog extends Animal {
    void bark() {
        System.out.println("Dog is barking");
    }
}

public class InheritanceExample {
    public static void main(String[] args) {
        Dog myDog = new Dog();
        myDog.eat(); // Inherits eat() method from Animal class
        myDog.bark(); // Calls bark() method from Dog class
    }
}
```

### ii. Polymorphism:
Polymorphism allows objects to be treated as instances of their superclass, even if they are instances of a subclass. This is achieved through method overriding (runtime polymorphism) or method overloading (compile-time polymorphism).

**Method Overriding Example:**
```java
// Parent class
class Shape {
    void draw() {
        System.out.println("Drawing a shape");
    }
}

// Subclass overriding the draw() method
class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a circle");
    }
}

public class PolymorphismExample {
    public static void main(String[] args) {
        Shape myShape = new Circle(); // Polymorphic behavior
        myShape.draw(); // Calls draw() of Circle class
    }
}
```

### iii. Encapsulation:
Encapsulation refers to bundling data (variables) and methods that operate on that data within a single unit (class), and controlling access to that data using access modifiers (like private, public, protected).

```java
// Encapsulation example
class Employee {
    private String name;
    private double salary;

    // Getter and setter methods
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public double getSalary() {
        return salary;
    }

    public void setSalary(double salary) {
        this.salary = salary;
    }
}

public class EncapsulationExample {
    public static void main(String[] args) {
        Employee emp = new Employee();
        emp.setName("John Doe");
        emp.setSalary(50000.0);
        System.out.println("Employee name: " + emp.getName());
        System.out.println("Employee salary: " + emp.getSalary());
    }
}
```

### iv. Abstraction:
Abstraction is the concept of hiding the complex implementation details and showing only the essential features of an object. Abstract classes and interfaces are used to achieve abstraction in Java.

**Abstract Class Example:**
```java
// Abstract class
abstract class Shape {
    abstract void draw(); // Abstract method (no implementation)
}

// Concrete subclass implementing the abstract method
class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a circle");
    }
}

public class AbstractionExample {
    public static void main(String[] args) {
        Shape myShape = new Circle(); // Polymorphic behavior
        myShape.draw(); // Calls draw() of Circle class
    }
}
```

In this example, `Shape` is an abstract class with an abstract method `draw()`. The `Circle` class extends `Shape` and provides an implementation for the `draw()` method, achieving abstraction.