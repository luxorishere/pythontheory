## Java Notes

### Unit 1

#### Introduction (First Part)

- Why Java
- History of Java
- JVM (Java Virtual Machine)
- JRE (Java Runtime Environment)
- Java Environment
- Java Source File Structure
- Compilation

#### Fundamental Concepts in Java

- Programming Structures in Java
  - Defining classes in Java
  - Constructors
  - Methods
  - Access Specifiers
  - Static Members
  - Final Members
  - Comments
  - Data types
  - Variables
  - Operators
  - Control Flow
  - Arrays & Strings

#### Object-Oriented Programming

- Class
- Object
- Inheritance
  - Superclass
  - Subclass
- Overriding
- Overloading
- Encapsulation
- Polymorphism
- Abstraction
- Interfaces
- Abstract Class

#### Packages

- Defining Packages
- CLASSPATH Setting for Packages
- Making JAR Files for Library Packages
- Import and Static Import Naming Convention For Packages

## Introduction

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

## Fundamental Concepts in Java

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

## Object-Oriented Programming

### Class
A class is a blueprint or template for creating objects. It defines the properties and behaviors that an object of that class will have.

```java
// Example of defining a class
public class MyClass {
    // Fields (attributes)
    int myField;
}
```

### Object
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

#### Superclass and Subclass
Superclass is the class that is inherited from, and subclass is the class that inherits from the superclass.

```java
// Example of superclass and subclass
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

#### Overriding
Overriding occurs when a subclass provides a specific implementation of a method that is already defined in its superclass. This allows for runtime polymorphism, where the method that gets executed is determined at runtime based on the object's type.

**Parent obj = new Child();**

This is also known as Upsitting


### Runtime / Dyanmic Polymorphism

*What is dynamic Method overlaoding*

**Dynamic runtime dispatched**

It's a mechanism to a call to a overridden method is resolved at runtime rather than a compile time

That's why the name is Dyanmic Polymorphism



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
    public static void main(String[] args)

 {
        Animal myAnimal = new Dog();
        myAnimal.makeSound(); // Output: Bark
    }
}
```

#### Overloading
Overloading occurs when two or more methods in the same class have the same name but different parameters (number, type, or both). Overloaded methods provide different ways to perform similar actions.

```java
class MathOperations {
    int add(int a, int b) {
        return a + b;
    }
    
    double add(double a, double b) {
        return a + b;
    }
    
    int add(int a, int b, int c) {
        return a + b + c;
    }
}

public class Main {
    public static void main(String[] args) {
        MathOperations math = new MathOperations();
        System.out.println(math.add(2, 3)); // Output: 5
        System.out.println(math.add(2.5, 3.5)); // Output: 6.0
        System.out.println(math.add(1, 2, 3)); // Output: 6
    }
}
```

### Encapsulation
Encapsulation is the practice of wrapping data (fields) and methods (behaviors) that operate on the data into a single unit or class. It is used to protect the internal state of an object and only allow controlled access through public methods.

```java
class Person {
    private String name;
    private int age;
    
    // Getter method for name
    public String getName() {
        return name;
    }
    
    // Setter method for name
    public void setName(String name) {
        this.name = name;
    }
    
    // Getter method for age
    public int getAge() {
        return age;
    }
    
    // Setter method for age
    public void setAge(int age) {
        if (age > 0) {
            this.age = age;
        }
    }
}

public class Main {
    public static void main(String[] args) {
        Person person = new Person();
        person.setName("John");
        person.setAge(25);
        System.out.println("Name: " + person.getName());
        System.out.println("Age: " + person.getAge());
    }
}
```

### Polymorphism
Polymorphism is the ability of an object to take on many forms. It allows one interface to be used for a general class of actions. The specific action is determined by the exact nature of the situation.

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

class Cat extends Animal {
    @Override
    void makeSound() {
        System.out.println("Meow");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myDog = new Dog();
        Animal myCat = new Cat();
        
        myDog.makeSound(); // Output: Bark
        myCat.makeSound(); // Output: Meow
    }
}
```

### Abstraction
Abstraction is the concept of hiding the complex implementation details of a system and exposing only the necessary and relevant parts to the user. It can be achieved using abstract classes and interfaces.

```java
abstract class Animal {
    abstract void makeSound(); // Abstract method
}

class Dog extends Animal {
    @Override
    void makeSound() {
        System.out.println("Bark");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myDog = new Dog();
        myDog.makeSound(); // Output: Bark
    }
}
```

### Interfaces
Interfaces are used to achieve abstraction in Java. They define a contract that implementing classes must follow. An interface can contain abstract methods and static constants.

```java
interface Animal {
    void makeSound(); // Abstract method
}

class Dog implements Animal {
    @Override
    public void makeSound() {
        System.out.println("Bark");
    }
}

public class Main {
    public static void main(String[] args) {
        Animal myDog = new Dog();
        myDog.makeSound(); // Output: Bark
    }
}
```

### Abstract Class
An abstract class is a class that cannot be instantiated and is meant to be subclassed. It can have abstract methods (without implementation) as well as concrete methods (with implementation).

```java
abstract class Animal {
    abstract void makeSound(); // Abstract method
    
    void sleep() {
        System.out.println("Sleeping...");
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
        Animal myDog = new Dog();
        myDog.makeSound(); // Output: Bark
        myDog.sleep(); // Output: Sleeping...
    }
}
```

## Packages

### Defining Packages
Packages are used to group related classes and interfaces together. They help to avoid name conflicts and make it easier to manage large codebases.

```java
// Define a package
package com.example.myapp;

public class MyClass {
    // Class implementation
}
```

### CLASSPATH Setting for Packages
The `CLASSPATH` environment variable is used to specify the location of user-defined classes and packages. It tells the Java compiler and JVM where to look for classes.

### Making JAR Files for Library Packages
JAR (Java ARchive) files are used to package multiple Java classes, metadata, and resources into a single file for distribution.

```bash
# Create a JAR file
jar cvf mylibrary.jar com/example/myapp/*.class
```

### Import and Static Import Naming Convention For Packages
The `import` statement is used to include classes and packages into your code. The `static import` statement allows the static members of a class to be used without specifying the class name.

```java
// Import a package
import java.util.*;

// Import a specific class
import java.util.ArrayList;

// Static import
import static java.lang.Math.*;
```

