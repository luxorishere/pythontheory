## Java Notes

### Unit 1

Introduction (First Part)
------------

- Why Java
- History of Java
- JVM (Java Virtual Machine)
- JRE (Java Runtime Environment)
- Java Environment
- Java Source File Structure
- Compilation

Fundamental concepts in Java
--------------------------------

- Programming Structures in Java
	+ Defining classes in Java
	+ Constructors
	+ Methods
	+ Access Specifiers
	+ Static Members
	+ Final Members
	+ Comments
	+ Data types
	+ Variables
	+ Operators
	+ Control Flow
	+ Arrays & Strings

Object Oriented Programming
-------------------------------

- Class
- Object
- Inheritance
	+ Super class
	+ Sub class
- Overriding
- Overloading
- Encapsulation
- Polymorphism
- Abstraction
- Interfaces
- Abstract Class

Packages
--------

- Defining Packages
- CLASSPATH Setting for Packages
- Making JAR Files for Library Packages
- Import and Static Import Naming Convention For Packages


## Introduction *First Part*
### Java
Java is a high-level, object-oriented programming language developed by Sun Microsystems (now owned by Oracle) in the mid-1990s. It is known for its platform independence and robustness.

### History of Java
Java was created by James Gosling at Sun Microsystems and released in 1995. It was designed to be portable, secure, and easy to use for developing a wide range of applications.

### JVM (Java Virtual Machine)
JVM is an abstract computing machine that provides the runtime environment for Java bytecode to be executed. It translates Java bytecode into native machine code and handles memory management, garbage collection, and other runtime tasks.

### JRE (Java Runtime Environment)
JRE is a software package that includes JVM, Java libraries, and other necessary components to run Java applications. It does not include development tools like compilers.

### Java Environment
Java Environment refers to the complete setup required for Java development and execution, including JDK (Java Development Kit), IDEs (Integrated Development Environments), and runtime environments like JRE or JVM.

### Java Source File Structure
A Java source file typically consists of a single public class and other supporting non-public classes. It includes package declarations, import statements, class declarations, fields, methods, and other elements according to Java syntax rules.

### Compilation
Compilation is the process of converting human-readable Java source code into platform-independent bytecode using a Java compiler (e.g., `javac`). This bytecode can then be executed by the JVM on any platform that supports Java.

## Fundamental concepts in Java *Second Part*


### Defining Classes in Java
Classes in Java are blueprints for objects. They define attributes (fields) and behaviors (methods) that objects of that class will have.

```java
// Example of defining a class
public class MyClass {
    // Fields (attributes)
    int myField;

    // Methods (behaviors)
    void myMethod() {
        System.out.println("This is a method in MyClass");
    }
}
```

### Constructors
Constructors are special methods used to initialize objects when they are created. They have the same name as the class and do not have a return type.

```java
// Example of a constructor
public class MyClass {
    int myField;

    // Constructor
    public MyClass(int value) {
        myField = value;
    }
}
```

### Methods
Methods are functions defined inside a class that perform specific tasks or operations.

```java
// Example of a method
public class MyClass {
    void myMethod() {
        System.out.println("This is myMethod");
    }
}
```

### Access Specifiers
Access specifiers control the visibility of classes, fields, and methods in Java. There are four access specifiers: `public`, `private`, `protected`, and default (no specifier).

```java
// Example of access specifiers
public class MyClass {
    public int publicField;
    private int privateField;
    protected int protectedField;
    int defaultField; // Default access
}
```

### Static Members
Static members (fields or methods) belong to the class itself rather than any specific instance of the class. They are accessed using the class name.

```java
// Example of static member
public class MyClass {
    static int staticField;
    static void staticMethod() {
        System.out.println("This is a static method");
    }
}
```

### Final Members
Final members (fields or methods) cannot be changed once initialized (for fields) or defined (for methods).

```java
// Example of final member
public class MyClass {
    final int finalField = 10;
    final void finalMethod() {
        System.out.println("This is a final method");
    }
}
```

### Comments
Comments are used to add explanations or documentation to the code and are ignored by the compiler.

```java
// This is a single-line comment

/*
 * This is a
 * multi-line comment
 */
public class MyClass {
    // This is an inline comment
}
```

### Data Types and Variables
Java has several data types such as `int`, `double`, `boolean`, etc., used to define variables.

```java
// Example of data types and variables
public class MyClass {
    int number = 5; // Integer variable
    double pi = 3.14; // Double variable
    boolean isTrue = true; // Boolean variable
    String text = "Hello"; // String variable
}
```

### Operators
Java supports various operators like arithmetic, relational, logical, etc., used to perform operations on variables and values.

```java
// Example of operators
public class MyClass {
    int a = 5;
    int b = 3;
    int sum = a + b; // Addition operator
    boolean isGreaterThan = a > b; // Relational operator
    boolean logicalAnd = true && false; // Logical AND operator
}
```

### Control Flow
Control flow statements such as `if-else`, `switch`, `for`, `while`, etc., control the flow of execution in Java programs.

```java
// Example of control flow
public class MyClass {
    void checkNumber(int num) {
        if (num > 0) {
            System.out.println("Positive");
        } else if (num < 0) {
            System.out.println("Negative");
        } else {
            System.out.println("Zero");
        }
    }
}
```

### Arrays & Strings
Arrays store multiple values of the same data type, and strings represent sequences of characters in Java.

```java
// Example of arrays and strings
public class MyClass {
    // Array
    int[] numbers = {1, 2, 3, 4, 5};

    // String
    String text = "Hello, Java!";
}
```
## Object Oriented Programming *Third Part*

### Class

What is a class?

A class is a blueprint or template for creating objects. It defines the properties and behaviors that an object of that class will have.

```java
// Example of defining a class
public class MyClass {
    // Fields (attributes)
    int myField;
}
    
```

### Object

What is an object?

An object is an instance of a class. It contains the state and behavior of the class.

```java
// Example of creating an object
public class MyClass {
    public static void main(String[] args) {
        // Creating an object of MyClass
        MyClass myObject = new MyClass();
        
        // Calling the method of the object
        myObject.myMethod();
    }
    
    int myField;
    void myMethod() {
        System.out.println("This is myMethod");
    }
}
```

### Inheritance

Inheritance is a mechanism in object-oriented programming that allows one class to inherit the properties and behaviors of another class.

```java
// Example of inheritance
public class MyParentClass {
    int myField;
    void myMethod() {
        System.out.println("This is myMethod");
    }
}

class MyChildClass extends MyParentClass {
    // This class inherits all the properties and methods of MyParentClass
    // and we can define new properties and methods in this class
    int myChildField;
    void myChildMethod() {
        // call the method of the parent class
        super.myMethod();
        System.out.println("This is myChildMethod");
    }
}

```
### Super Class and Sub Class

Super class is the class that is inherited from and sub class is the class that inherits from the super class.

```java
// Example of super class and sub class
public class MyParentClass {
    int myField;
    void myMethod() {
        System.out.println("This is myMethod");
    }
}

class MyChildClass extends MyParentClass {
    // This class inherits all the properties and methods of MyParentClass
    // and we can define new properties and methods in this class
    int myChildField;
    void myChildMethod() {
        // call the method of the parent class
        super.myMethod();
        System.out.println("This is myChildMethod");
    }
    public static void main(String[] args) {
        MyChildClass myObject = new MyChildClass();
        myObject.myMethod();
        myObject.myChildMethod();
    }
}
```

1. **Overriding**: Overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. This allows for runtime polymorphism, where the method that gets executed is determined at runtime based on the object's type.

```java
class Animal {
    void makeSound() {
        System.out.println("Animal sound");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Bark");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Dog();
        animal.makeSound(); // Output: Bark
    }
}
```

2. **Overloading**: Overloading refers to defining multiple methods in a class with the same name but different parameters (number, type, or order). The compiler determines which method to call based on the arguments provided.

```java
class Calculator {
    int add(int a, int b) {
        return a + b;
    }

    double add(double a, double b) {
        return a + b;
    }
}

public class Main {
    public static void main(String[] args) {
        Calculator calc = new Calculator();
        System.out.println(calc.add(5, 10)); // Output: 15
        System.out.println(calc.add(3.5, 2.5)); // Output: 6.0
    }
}
```

3. **Encapsulation**: Encapsulation is the practice of bundling the data (attributes) and methods (behavior) that operate on the data into a single unit (class). It helps in hiding the internal state of an object and only exposing the necessary functionalities through methods.

```java
class Student {
    private String name;
    private int age;

    public void setName(String name) {
        this.name = name;
    }

    public void setAge(int age) {
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public int getAge() {
        return age;
    }
}

public class Main {
    public static void main(String[] args) {
        Student student = new Student();
        student.setName("Alice");
        student.setAge(20);
        System.out.println("Name: " + student.getName());
        System.out.println("Age: " + student.getAge());
    }
}
```

4. **Polymorphism**: Polymorphism allows objects to be treated as instances of their superclass, even if they are instances of a subclass. This can be achieved through method overriding (runtime polymorphism) or method overloading (compile-time polymorphism).

```java
class Shape {
    void draw() {
        System.out.println("Drawing a shape");
    }
}

class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a circle");
    }
}

public class Main {
    public static void main(String[] args) {
        Shape shape = new Circle();
        shape.draw(); // Output: Drawing a circle
    }
}
```

5. **Abstraction**: Abstraction is the process of hiding the implementation details and showing only the essential features of an object. Abstract classes and interfaces are used to achieve abstraction.

```java
abstract class Shape {
    abstract void draw();
}

class Circle extends Shape {
    @Override
    void draw() {
        System.out.println("Drawing a circle");
    }
}

public class Main {
    public static void main(String[] args) {
        Shape shape = new Circle();
        shape.draw(); // Output: Drawing a circle
    }
}
```

6. **Interfaces**: An interface in Java is a reference type that can contain only constants, method signatures, default methods, static methods, and nested types. It defines a set of methods that a class must implement, providing a contract for behavior.

```java
interface Printable {
    void print();
}

class Document implements Printable {
    @Override
    public void print() {
        System.out.println("Printing document");
    }
}

public class Main {
    public static void main(String[] args) {
        Printable printable = new Document();
        printable.print(); // Output: Printing document
    }
}
```

7. **Abstract Class**: An abstract class is a class that cannot be instantiated on its own and may contain abstract methods (methods without a body) that must be implemented by its subclasses. It can also contain concrete methods and instance variables.

```java
abstract class Animal {
    abstract void makeSound();

    void eat() {
        System.out.println("Animal eating");
    }
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Bark");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal animal = new Dog();
        animal.makeSound(); // Output: Bark
        animal.eat(); // Output: Animal eating
    }
}
```

## Packages


1. **Defining Packages**:
   - A package in Java is a way to organize related classes and interfaces. It helps avoid naming conflicts and provides a namespace for the classes.
   - Packages are defined at the beginning of your Java source file using the `package` keyword followed by the package name.
   - For example, let's say we have a package named `com.example.utilities`:

```java
package com.example.utilities;

public class MathUtils {
    public static int add(int a, int b) {
        return a + b;
    }
}
```

2. **CLASSPATH Setting for Packages**:
   - CLASSPATH is an environment variable that tells the Java compiler and runtime where to look for classes and packages.
   - When you compile and run Java programs that use packages, you need to set the CLASSPATH to include the directory containing your packages.
   - You can set the CLASSPATH using command-line options or by setting the environment variable. For example:

```bash
# Command-line option
javac -cp path/to/your/packages Main.java

# Environment variable (Linux/macOS)
export CLASSPATH=/path/to/your/packages

# Environment variable (Windows)
set CLASSPATH=C:\path\to\your\packages
```

3. **Making JAR Files for Library Packages**:
   - JAR (Java Archive) files are used to package Java classes and resources into a single file. They are commonly used for distributing libraries and applications.
   - To create a JAR file for your package, you can use the `jar` command provided by Java.
   - For example, let's create a JAR file for our `com.example.utilities` package:

```bash
# Create JAR file
jar cf myutils.jar -C /path/to/your/packages com/example/utilities
```

4. **Import and Static Import Naming Convention For Packages**:
   - Import statements are used to make classes and interfaces from other packages accessible in your code.
   - Regular import: `import package_name.class_name;`
   - Static import (Java 5 and above): `import static package_name.class_name.*;`
   - It's recommended to follow naming conventions when importing packages and classes:
     - Use lowercase for package names (e.g., `com.example.utilities`).
     - Use camelCase for class names (e.g., `MathUtils`).

Example usage with import statements:

```java
import com.example.utilities.MathUtils;

public class Main {
    public static void main(String[] args) {
        int sum = MathUtils.add(5, 10);
        System.out.println("Sum: " + sum);
    }
}
```

Example usage with static import:

```java
import static com.example.utilities.MathUtils.*;

public class Main {
    public static void main(String[] args) {
        int sum = add(5, 10);
        System.out.println("Sum: " + sum);
    }
}
```

### Try Exception Handling


Exception Handling:

- Exceptions are used to handle errors or exceptions that occur during the execution of a program.
- Exceptions are objects that are thrown when an error occurs.
- Exception handling is the process of writing code that will "handle" these exceptions in a way that is appropriate for the situation.
- Catch block is used to handle exceptions.
- Finally block is used to execute certain code whether an exception occurs or not.
- Java has a number of built-in exceptions, and it is also possible to create custom exceptions.

```java

public class ExceptionHandlingExample {
    public static void main(String[] args) {
        try {
            // Code that may cause an exception
            int result = 10 / 0; // This will throw an ArithmeticException
            System.out.println("Result: " + result); // This line won't be executed
        } catch (ArithmeticException e) {
            // Catching and handling the exception
            System.out.println("An arithmetic exception occurred: " + e.getMessage());
        }
        // The program continues execution after handling the exception
        System.out.println("Program execution continues...");
    }
}
```

### Multithreading

Multithreading in Java:

- Multithreading is the ability of a program to perform multiple tasks simultaneously.
- In Java, multithreading is achieved using threads. A thread is a separate flow of execution that can run concurrently with other threads in a program.
- Java provides a built-in support for multithreading using the `Thread` class.
- To create a thread in Java, you need to extend the `Thread` class or implement the `Runnable` interface.
- When a thread is created, it is in a new state called "New". The thread scheduler starts the thread by changing its state to "Runnable".
- When a thread is runnable, it is executed by the thread scheduler. The thread scheduler selects a runnable thread and executes it.
- If the thread scheduler is unable to find any runnable thread, it will put the current thread (the thread that is being executed) in the "Waiting" state.
- The thread scheduler will wake up a waiting thread when there is a runnable thread available.
- A thread can be in one of the following states: New, Runnable, Waiting, Timed Waiting, Blocked, Terminated.
- The `join()` method is used to wait for the completion of a thread.
- The `synchronized` keyword is used to provide mutual exclusion between threads.
- The `volatile` keyword is used to ensure that changes to a variable are immediately visible to all threads.
- The `wait()` and `notify()` methods are used to synchronize threads.
- The `notifyAll()` method is used to notify all threads that are waiting on an object.


```markdown
### Summarizing multithreading in Java in five lines:

- Multithreading allows a program to perform multiple tasks simultaneously.
- Java provides built-in support for multithreading using the `Thread` class.
- Threads execute concurrently with other threads in a program, and the thread scheduler manages the execution of threads.
- Threads can also be in the "Blocked" state, which means that the thread is waiting for a lock to be released.
- The thread scheduler will wake up a blocked thread when the lock is released.
```
```java
public class MultithreadingExample {
    public static void main(String[] args) {
        // Create and start a new thread using Runnable interface
        Thread thread1 = new Thread(new MyRunnable());
        thread1.start();

        // Create and start a new thread by extending Thread class
        MyThread thread2 = new MyThread();
        thread2.start();

        // Main thread continues execution
        System.out.println("Main thread is running...");
    }

    // Runnable implementation for creating threads
    static class MyRunnable implements Runnable {
        @Override
        public void run() {
            // Code that runs in the new thread
            for (int i = 0; i < 5; i++) {
                System.out.println("Runnable thread: " + i);
                try {
                    Thread.sleep(1000); // Sleep for 1 second
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }

    // Thread class extension for creating threads
    static class MyThread extends Thread {
        @Override
        public void run() {
            // Code that runs in the new thread
            for (int i = 0; i < 5; i++) {
                System.out.println("Thread class thread: " + i);
                try {
                    Thread.sleep(1000); // Sleep for 1 second
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        }
    }
}
```

### Shorter Code

```java
public class MultithreadingExample {
    public static void main(String[] args) {
        // Creating and starting a thread using lambda expression
        Thread thread1 = new Thread(() -> {
            for (int i = 0; i < 5; i++) {
                System.out.println("Thread 1: " + i);
                try {
                    Thread.sleep(1000); // Sleep for 1 second
                } catch (InterruptedException e) {
                    e.printStackTrace();
                }
            }
        });
        thread1.start();

        // Creating and starting a thread using anonymous class
        Thread thread2 = new Thread(new Runnable() {
            @Override
            public void run() {
                for (int i = 0; i < 5; i++) {
                    System.out.println("Thread 2: " + i);
                    try {
                        Thread.sleep(1000); // Sleep for 1 second
                    } catch (InterruptedException e) {
                        e.printStackTrace();
                    }
                }
            }
        });
        thread2.start();

        // Main thread continues execution
        System.out.println("Main thread is running...");
    }
}
```

### Thread life cycle

Thread Life Cycle

------------------

1. New: A thread is created using the `Thread` constructor or by implementing the `Runnable` interface.
2. Runnable: The thread becomes runnable when it is started using the `start()` method.
3. Running: The thread is executing the code inside the `run()` method.
4. Blocked: The thread is waiting for a resource to become available, such as a lock or a condition variable.
5. Waiting: The thread has finished executing the `run()` method and is waiting to be joined by another thread.
6. Terminated: The thread has completed execution and is no longer running.

Note that a thread can be in multiple states at the same time, for example, a thread can be both runnable and blocked.

```java
public class ThreadLifecycleExample {
    public static void main(String[] args) {
        Thread thread = new Thread(() -> {
            System.out.println("Thread is in NEW state"); // New state
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
            System.out.println("Thread is in RUNNABLE state"); // Runnable state
        });

        System.out.println("Thread is created but not yet started"); // New state
        thread.start(); // Transition to Runnable state

        try {
            Thread.sleep(2000);
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println("Thread is in TERMINATED state"); // Terminated state
    }
}
```

<!-- SET JAVA HOME PATH -->
