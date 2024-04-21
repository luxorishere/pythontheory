## JRE and JVM
**JRE (Java Runtime Environment):**
- Stands for Java Runtime Environment.
- Provides necessary libraries and components to run Java applications.

**JVM (Java Virtual Machine):**
- Stands for Java Virtual Machine.
- Executes Java bytecode and provides a platform-independent runtime environment for Java programs.
## Operators

```java
public class OperatorsExample {
    public static void main(String[] args) {
        // Arithmetic operators
        int sum = a + b;
        int difference = a - b;
        int product = a * b;
        int quotient = a / b;
        int remainder = a % b;

        // Relational operators
        boolean isEqual = a == b;
        boolean isNotEqual = a != b;
        boolean isGreaterThan = a > b;
        boolean isLessThan = a < b;

        // Logical operators
        boolean isTrue = true;
        boolean isFalse = false;
        boolean andResult = isTrue && isFalse;
        boolean orResult = isTrue || isFalse;
        boolean notResult = !isTrue;

    
    }
}
```

```java
public class MyJavaProgram {
    public static void main(String[] args) {
        // Code statements
        System.out.println("Hello, Java!");
    }
}
```


## Arrays

Arrays in Java are used to store multiple values of the same data type in a single variable. They provide indexed access to elements and are fixed in size once declared.

## Break and Continue

```java
public class BreakContinueExample {
    public static void main(String[] args) {
        // Example of break statement
        System.out.println("Example of break statement:");
        for (int i = 1; i <= 5; i++) {
            if (i == 3) {
                break; // Exit the loop when i equals 3
            }
            System.out.println("Value of i: " + i);
        }

        // Example of continue statement
        System.out.println("\nExample of continue statement:");
        for (int j = 1; j <= 5; j++) {
            if (j == 3) {
                continue; // Skip the current iteration when j equals 3
            }
            System.out.println("Value of j: " + j);
        }
    }
}
```

In this example:
- The `break` statement is used inside a `for` loop to exit the loop when the value of `i` is equal to 3. This means only values of `i` from 1 to 2 will be printed.
- The `continue` statement is used inside another `for` loop to skip the current iteration when the value of `j` is equal to 3. This means the value of `j` equal to 3 will not be printed, but the loop continues to the next iteration.

## Loops 

1. **for loop**: Executes a block of code repeatedly based on a specified condition, typically used for iterating over a range of values.

2. **while loop**: Repeats a block of code while a given condition is true, checking the condition before each iteration.

3. **do-while loop**: Similar to a while loop, but it always executes the block of code at least once before checking the condition for subsequent iterations.
 
# Modifier

1. **Default (Package-Private)**: Accessible within the same package only.
2. **Public**: Accessible from any class in any package.
3. **Private**: Accessible only within the same class.
4. **Protected**: Accessible within the same package and by subclasses, even in different packages.Certainly:

## Final and Static

1. **Final Keyword**: Indicates that a variable's value cannot be changed once assigned or a method cannot be overridden.

2. **Static Keyword**: Denotes that a variable or method belongs to the class rather than instances of the class.

Example:
```java
public class Example {
    public static final int MAX_VALUE = 100; // Final and static variable

    public static void main(String[] args) {
        // Accessing static final variable
        System.out.println("Max value: " + Example.MAX_VALUE);
        
        // Attempting to modify the final variable (will result in a compilation error)
        // Example.MAX_VALUE = 200; // Error: cannot assign a value to final variable
    }
}
```

# OOP Concepts

i. **Inheritance**:
```java
class Animal { } // Superclass

class Dog extends Animal { } // Subclass
```

ii. **Polymorphism**:
```java
class Animal {
    void makeSound() { } // Common method
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Dog is barking");
    }
}
```

iii. **Encapsulation**:
```java
class Person {
    private String name; // Private data member

    public String getName() { return name; } // Getter method
    public void setName(String name) { this.name = name; } // Setter method
}
```

iv. **Abstraction**:
```java
abstract class Shape {
    abstract void draw(); // Abstract method without implementation
}

class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a circle");
    }
}
```
