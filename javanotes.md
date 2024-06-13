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

## Unit 3
### Syllabus in one shot

- *Functional Interfaces*: Interfaces with a single abstract method, enabling lambda expressions.

- *Lambda Expressions*: Concise syntax for defining anonymous functions, enhancing code readability, and enabling functional programming paradigms.

- *Method References*: Simplified syntax for referencing methods without invoking them directly.

- Stream API: Enables functional-style operations on sequences of elements, promoting efficient and concise code.

- Default Methods: Methods within interfaces with default implementations, facilitating interface evolution without breaking existing implementations.

- *Static Method*: Methods that can be called directly on a class without needing an instance.

- *Base64 Encode and Decode*: Functions for encoding and decoding data in Base64 format.

- Each Method: Simplified iteration over collections using lambda expressions.

- *Try-with-resources*: Automatic resource management by ensuring resources are closed after being used.

- *Type Annotations*: Annotations that can be applied to types to provide additional type information.

- Repeating Annotations: Annotations that can be applied multiple times to a declaration.

- *Java Module System*: Enables modular programming by encapsulating code into modules with explicit dependencies.

- Diamond Syntax with Anonymous Class: Simplified syntax for creating instances of anonymous classes using the diamond operator.

- Inner Anonymous Class: Anonymous class defined within another class without a name.

- *Local Variable Type Inference*: Allows the compiler to infer the type of local variables, reducing verbosity in code.

- *Switch Expressions*: Enhanced switch statement that can return a value, improving code expressiveness.

- Yield Keyword: Used in switch expressions to return a value and terminate the switch block.

- Text Blocks: Multi-line string literals for improved readability of large text blocks.

- Records: Concise data carrier classes with auto-generated methods like constructors, getters, equals, and hashcode.

- Sealed Classes: Classes that restrict which other classes can extend or implement them, enhancing code safety and maintainability.
# Functional Interfaces (imp)

## Definition
Functional Interfaces are interfaces that have only one abstract method. They can contain multiple default or static methods. They are - often used in conjunction with lambda expressions and method references.

## Code
```java
@FunctionalInterface
interface MyFunctionalInterface {
    void myMethod();
}
```

# Lambda Expression

## Definition
Lambda expressions are a way to provide concise implementations of functional interfaces. They are essentially anonymous functions that can be used to replace instances of functional interfaces.

## Code
```java
MyFunctionalInterface myFunc = () -> System.out.println("Hello Lambda!");
myFunc.myMethod();
```

# Method References

## Definition
Method references are a shorthand notation of a lambda expression to call a method. They use the `::` operator.

## Code
```java
import java.util.Arrays;
import java.util.List;

class MethodReferenceExample {
    public static void printMessage(String message) {
        System.out.println(message);
    }

    public static void main(String[] args) {
        List<String> messages = Arrays.asList("Hello", "World");
        messages.forEach(MethodReferenceExample::printMessage);
    }
}
```

# Stream API

## Definition
The Stream API is used to process collections of objects in a functional style. It allows operations like filtering, mapping, and reducing.

## Code
```java
import java.util.Arrays;
import java.util.List;
import java.util.stream.Collectors;

class StreamAPIExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
        List<String> filteredNames = names.stream()
                                          .filter(name -> name.startsWith("A"))
                                          .collect(Collectors.toList());
        System.out.println(filteredNames);
    }
}
```

# Default Methods

## Definition
Default methods are methods in an interface that have a default implementation. They allow adding new methods to interfaces without breaking existing implementations.

## Code
```java
interface MyInterface {
    default void defaultMethod() {
        System.out.println("This is a default method.");
    }
}

class MyClass implements MyInterface {
    // No need to override defaultMethod
}

public class DefaultMethodExample {
    public static void main(String[] args) {
        MyClass myClass = new MyClass();
        myClass.defaultMethod();
    }
}
```

# Static Method

## Definition
Static methods in interfaces are methods that belong to the interface rather than any particular instance. They can be called without an object of the class.

## Code
```java
interface MyInterface {
    static void staticMethod() {
        System.out.println("This is a static method.");
    }
}

public class StaticMethodExample {
    public static void main(String[] args) {
        MyInterface.staticMethod();
    }
}
```

# Base64 Encode and Decode

## Definition
Base64 encoding and decoding are mechanisms to encode binary data into a textual format and decode it back.

## Code
```java
import java.util.Base64;

public class Base64Example {
    public static void main(String[] args) {
        String originalInput = "Hello World!";
        String encodedString = Base64.getEncoder().encodeToString(originalInput.getBytes());
        String decodedString = new String(Base64.getDecoder().decode(encodedString));

        System.out.println("Encoded: " + encodedString);
        System.out.println("Decoded: " + decodedString);
    }
}
```

# ForEach Method

## Definition
The `forEach` method is used to iterate over elements of a collection and perform an action on each element.

## Code
```java
import java.util.Arrays;
import java.util.List;

public class ForEachExample {
    public static void main(String[] args) {
        List<String> names = Arrays.asList("Alice", "Bob", "Charlie");
        names.forEach(name -> System.out.println(name));
    }
}
```

# Try-with-resources

## Definition
The try-with-resources statement ensures that each resource is closed at the end of the statement. It works with any object that implements `java.lang.AutoCloseable`.

## Code
```java
import java.io.BufferedReader;
import java.io.FileReader;
import java.io.IOException;

public class TryWithResourcesExample {
    public static void main(String[] args) {
        try (BufferedReader br = new BufferedReader(new FileReader("test.txt"))) {
            System.out.println(br.readLine());
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
```

# Type Annotations

## Definition
Type annotations are annotations that can be applied to any use of a type. They are used to provide additional information about the type.

## Code
```java
import java.lang.annotation.ElementType;
import java.lang.annotation.Target;

@Target(ElementType.TYPE_USE)
@interface NonNull {}

public class TypeAnnotationsExample {
    public static void main(String[] args) {
        @NonNull String str = "Hello";
        System.out.println(str);
    }
}
```

# Repeating Annotations

## Definition
Repeating annotations allow the same annotation to be applied multiple times to the same declaration or type use.

## Code
```java
import java.lang.annotation.*;

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
@Repeatable(Schedules.class)
@interface Schedule {
    String day();
}

@Retention(RetentionPolicy.RUNTIME)
@Target(ElementType.TYPE)
@interface Schedules {
    Schedule[] value();
}

@Schedule(day = "Monday")
@Schedule(day = "Wednesday")
class RepeatingAnnotationsExample {
    public static void main(String[] args) {
        Schedule[] schedules = RepeatingAnnotationsExample.class.getAnnotationsByType(Schedule.class);
        for (Schedule schedule : schedules) {
            System.out.println("Day: " + schedule.day());
        }
    }
}
```

# Java Module System

## Definition
The Java Module System (introduced in Java 9) allows developers to group related packages and resources together, control the accessibility of these packages, and ensure strong encapsulation.

## Code
```java
// module-info.java
module com.example.myapp {
    exports com.example.myapp;
}
```

# Diamond Syntax with Anonymous Class

## Definition
The diamond syntax (`<>`) can be used with anonymous classes to infer type parameters.

## Code
```java
import java.util.ArrayList;
import java.util.List;

public class DiamondSyntaxExample {
    public static void main(String[] args) {
        List<String> list = new ArrayList<>() {
            {
                add("Hello");
                add("World");
            }
        };
        list.forEach(System.out::println);
    }
}
```

# Inner Anonymous Class

## Definition
An inner anonymous class is a class without a name that is defined and instantiated all at once. It is often used to implement interfaces or extend classes in a concise way.

## Code
```java
public class InnerAnonymousClassExample {
    interface Greeting {
        void sayHello();
    }

    public static void main(String[] args) {
        Greeting greeting = new Greeting() {
            @Override
            public void sayHello() {
                System.out.println("Hello, World!");
            }
        };
        greeting.sayHello();
    }
}
```

# Local Variable Type Inference

## Definition
Local Variable Type Inference allows the `var` keyword to be used to infer the type of local variables based on their initializer.

## Code
```java
public class LocalVariableTypeInferenceExample {
    public static void main(String[] args) {
        var message = "Hello, World!";
        System.out.println(message);
    }
}
```

# Switch Expressions

## Definition
Switch expressions (introduced in Java 12) allow the use of switch as an expression rather than a statement, simplifying many switch-case scenarios.

## Code
```java
public class SwitchExpressionExample {
    public static void main(String[] args) {
        var day = "TUESDAY";
        var result = switch (day) {
            case "MONDAY", "FRIDAY", "SUNDAY" -> "1st, 5th or 7th day";
            case "TUESDAY" -> "2nd day";
            case "THURSDAY", "SATURDAY" -> "4th or 6th day";
            case "WEDNESDAY" -> "3rd day";
            default -> "Invalid day";
        };
        System.out.println(result);
    }
}
```

# Yield Keyword

## Definition
The `yield` keyword is used in switch expressions to return a value from a case block.

## Code
```java
public class YieldKeywordExample {
    public static void main(String[] args) {
        var day = "WEDNESDAY";
        var result = switch (day) {
            case "MONDAY" -> "Start of the work week";
            case "WEDNESDAY" -> {
                yield "Midweek";
            }
            case "FRIDAY" -> "End of the work week";
            default -> "Other day";
        };
        System.out.println(result);
    }
}
```

# Text Blocks

## Definition
Text blocks (introduced in Java 13) are multi-line string literals that help improve the readability and maintainability of strings that span multiple lines.

## Code
```java
public class TextBlocksExample {
    public static void main(String[] args) {
        var textBlock = """
                This is a text block.
                It spans multiple lines.
                """;
        System.out.println(textBlock);
    }
}
```

# Records

## Definition
Records (introduced in Java 14) are a special kind of class in Java that is designed to hold immutable data. They automatically generate boilerplate code like constructors, getters, `equals`, `hashCode`, and `toString`.

## Code
```java
public record Person(String

 name, int age) {}

public class RecordsExample {
    public static void main(String[] args) {
        var person = new Person("Alice", 30);
        System.out.println(person.name());
        System.out.println(person.age());
    }
}
```

# Sealed Classes

## Definition
Sealed classes (introduced in Java 15) allow a class to control which other classes or interfaces can extend or implement it. They provide a more declarative way of defining class hierarchies.

## Code
```java
public sealed class Shape permits Circle, Rectangle {}

final class Circle extends Shape {}
final class Rectangle extends Shape {}

public class SealedClassesExample {
    public static void main(String[] args) {
        Shape shape1 = new Circle();
        Shape shape2 = new Rectangle();
        System.out.println("Created shapes: " + shape1 + ", " + shape2);
    }
}
```

# Unit 4: Java Collections Framework

## Collection in Java
A **Collection** is like a container that holds a group of objects, often referred to as elements. It's similar to a basket where you can store and organize items.

## Collection Framework in Java
The **Collection Framework** is a set of classes and interfaces that implement commonly reusable collection data structures. Think of it as a toolbox with different types of storage containers.

## Hierarchy of Collection Framework
The hierarchy of the Collection Framework can be visualized like a family tree, showing the relationships between interfaces and classes.

## Iterator Interface
The **Iterator** interface provides methods to traverse a collection. It's like having a remote control to navigate through channels (elements).

```java
Iterator<String> iterator = collection.iterator();
while (iterator.hasNext()) {
    System.out.println(iterator.next());
}
```

## Collection Interface
The **Collection** interface is the root of the collection hierarchy. It's like the base template for all types of collections.

```java
Collection<String> collection = new ArrayList<>();
```

## List Interface
The **List** interface represents an ordered collection, like a shopping list where order matters.

```java
List<String> list = new ArrayList<>();
```

## ArrayList
An **ArrayList** is a resizable array. It's like a dynamic array that can grow as needed.

```java
ArrayList<String> arrayList = new ArrayList<>();
arrayList.add("Apple");
```

## LinkedList
A **LinkedList** is a list where each element points to the next. It's like a chain where each link knows the next link.

```java
LinkedList<String> linkedList = new LinkedList<>();
linkedList.add("Banana");
```

## Vector
A **Vector** is similar to an ArrayList but synchronized. It's like an ArrayList with a security guard ensuring thread safety.

```java
Vector<String> vector = new Vector<>();
vector.add("Cherry");
```

## Stack
A **Stack** follows LIFO (Last In, First Out). It's like a stack of plates where you can only take the top one.

```java
Stack<String> stack = new Stack<>();
stack.push("Plate1");
String top = stack.pop();
```

## Queue Interface
A **Queue** follows FIFO (First In, First Out). It's like a line at the ticket counter where the first person in line is served first.

```java
Queue<String> queue = new LinkedList<>();
queue.add("Person1");
String next = queue.poll();
```

## Set Interface
A **Set** is a collection that cannot contain duplicate elements. It's like a guest list where each name must be unique.

```java
Set<String> set = new HashSet<>();
set.add("John");
```

## HashSet
A **HashSet** is a Set backed by a hash table. It's like a guest list where names are stored in a hash table for quick lookup.

```java
HashSet<String> hashSet = new HashSet<>();
hashSet.add("Jane");
```

## LinkedHashSet
A **LinkedHashSet** maintains insertion order. It's like a guest list that remembers the order in which guests were added.

```java
LinkedHashSet<String> linkedHashSet = new LinkedHashSet<>();
linkedHashSet.add("Doe");
```

## SortedSet Interface
A **SortedSet** is a Set that maintains its elements in ascending order. It's like a sorted guest list.

```java
SortedSet<String> sortedSet = new TreeSet<>();
sortedSet.add("Alice");
```

## TreeSet
A **TreeSet** is a NavigableSet implementation based on a TreeMap. It's like a sorted guest list backed by a tree structure.

```java
TreeSet<String> treeSet = new TreeSet<>();
treeSet.add("Bob");
```

## Map Interface
A **Map** is a collection of key-value pairs. It's like a dictionary where you look up values using keys.

```java
Map<String, String> map = new HashMap<>();
map.put("Key1", "Value1");
```

## HashMap Class
A **HashMap** is a Map based on a hash table. It's like a dictionary implemented using a hash table for fast access.

```java
HashMap<String, String> hashMap = new HashMap<>();
hashMap.put("Apple", "Fruit");
```

## LinkedHashMap Class
A **LinkedHashMap** maintains insertion order. It's like a hash map that remembers the order entries were added.

```java
LinkedHashMap<String, String> linkedHashMap = new LinkedHashMap<>();
linkedHashMap.put("Banana", "Fruit");
```

## TreeMap Class
A **TreeMap** is a Red-Black tree-based implementation of the Map interface. It's like a sorted dictionary.

```java
TreeMap<String, String> treeMap = new TreeMap<>();
treeMap.put("Cherry", "Fruit");
```

## Hashtable Class
A **Hashtable** is synchronized and does not allow null keys or values. It's like a thread-safe dictionary.

```java
Hashtable<String, String> hashtable = new Hashtable<>();
hashtable.put("Date", "Fruit");
```

## Sorting
**Sorting** is arranging elements in a particular order. It's like organizing books on a shelf alphabetically.

## Comparable Interface
The **Comparable** interface imposes a natural ordering on objects. It's like specifying how to compare two books.

```java
class Book implements Comparable<Book> {
    String title;

    public int compareTo(Book b) {
        return this.title.compareTo(b.title);
    }
}
```

## Comparator Interface
The **Comparator** interface provides an alternative comparison. It's like having different criteria to sort books.

```java
class BookComparator implements Comparator<Book> {
    public int compare(Book b1, Book b2) {
        return b1.title.compareTo(b2.title);
    }
}
```

## Properties Class in Java
The **Properties** class represents a persistent set of properties. It's like a file where you store configuration settings.

```java
Properties properties = new Properties();
properties.setProperty("username", "admin");
```

Sure, I'll provide brief explanations for each topic according to the marks allocated, ensuring the language is simple and focused on Java OOP.

### Memory Hierarchy (5 marks)
Memory hierarchy refers to the different levels of storage used by a computer system to manage data efficiently. These levels include:

1. **Registers**: Small, fast storage locations within the CPU used for temporary data storage during processing.
2. **Cache**: Faster than main memory (RAM), used to store frequently accessed data to speed up processing.
3. **Main Memory (RAM)**: Primary storage used to hold data and programs currently in use.
4. **Secondary Storage**: Includes hard drives and SSDs, used for long-term data storage, slower but larger capacity than RAM.
5. **Tertiary Storage**: External storage like tapes and optical discs, used for backup and archival purposes, slower but very high capacity.

### Base Encoder (10 marks)
In Java, a Base Encoder typically refers to encoding data into Base64 format. Base64 is a way to encode binary data into text using 64 different ASCII characters. It is often used to encode data for transmission over text-based protocols like HTTP.

- **Encoding**:
  ```java
  import java.util.Base64;
  
  public class Base64Encoder {
      public static void main(String[] args) {
          String originalInput = "Hello, World!";
          String encodedString = Base64.getEncoder().encodeToString(originalInput.getBytes());
          System.out.println(encodedString); // Outputs encoded string
      }
  }
  ```

- **Decoding**:
  ```java
  import java.util.Base64;
  
  public class Base64Decoder {
      public static void main(String[] args) {
          String encodedString = "SGVsbG8sIFdvcmxkIQ==";
          byte[] decodedBytes = Base64.getDecoder().decode(encodedString);
          String decodedString = new String(decodedBytes);
          System.out.println(decodedString); // Outputs: Hello, World!
      }
  }
  ```

### Priority Queue (10 marks)
A Priority Queue in Java is a data structure that stores elements in a way that allows for efficient retrieval of the highest (or lowest) priority element.

- **Using PriorityQueue**:
  ```java
  import java.util.PriorityQueue;

  public class PriorityQueueExample {
      public static void main(String[] args) {
          PriorityQueue<Integer> pq = new PriorityQueue<>();
          pq.add(5);
          pq.add(1);
          pq.add(3);

          while (!pq.isEmpty()) {
              System.out.println(pq.poll()); // Outputs elements in ascending order: 1, 3, 5
          }
      }
  }
  ```

### Try with Resources (5 marks)
The try-with-resources statement in Java ensures that resources (like files, database connections) are automatically closed after use.

- **Example**:
  ```java
  import java.io.BufferedReader;
  import java.io.FileReader;
  import java.io.IOException;

  public class TryWithResourcesExample {
      public static void main(String[] args) {
          try (BufferedReader br = new BufferedReader(new FileReader("file.txt"))) {
              String line;
              while ((line = br.readLine()) != null) {
                  System.out.println(line);
              }
          } catch (IOException e) {
              e.printStackTrace();
          }
      }
  }
  ```

### Functional Interface with Lambda Expressions (5 marks)
A functional interface in Java is an interface with a single abstract method. Lambda expressions provide a clear and concise way to implement these interfaces.

- **Example**:
  ```java
  @FunctionalInterface
  interface Greeting {
      void sayHello(String name);
  }

  public class LambdaExample {
      public static void main(String[] args) {
          Greeting greet = (name) -> System.out.println("Hello, " + name);
          greet.sayHello("World"); // Outputs: Hello, World
      }
  }
  ```

### Annotations (2 marks)
Annotations in Java provide metadata about the code. They can be used for various purposes like documentation, code analysis, and even at runtime.

- **Example**:
  ```java
  @Override
  public String toString() {
      return "Example";
  }
  ```

### Iterator Interface (2 marks)
The Iterator interface provides a way to traverse a collection of objects.

- **Example**:
  ```java
  import java.util.ArrayList;
  import java.util.Iterator;
  import java.util.List;

  public class IteratorExample {
      public static void main(String[] args) {
          List<String> list = new ArrayList<>();
          list.add("A");
          list.add("B");
          list.add("C");

          Iterator<String> iterator = list.iterator();
          while (iterator.hasNext()) {
              System.out.println(iterator.next()); // Outputs: A, B, C
          }
      }
  }
  ```

### Switch Statements and Expressions (2 marks)
Switch statements in Java allow a variable to be tested against multiple values. As of Java 12, switch expressions provide a more concise syntax.

- **Example**:
  ```java
  int day = 2;
  switch (day) {
      case 1 -> System.out.println("Monday");
      case 2 -> System.out.println("Tuesday"); // Outputs: Tuesday
      default -> System.out.println("Other day");
  }
  ```

### Yield Keyword (2 marks)
The `yield` keyword in Java is used in switch expressions to return a value.

- **Example**:
  ```java
  int day = 2;
  String dayName = switch (day) {
      case 1 -> "Monday";
      case 2 -> {
          yield "Tuesday"; // Returns: Tuesday
      }
      default -> "Other day";
  };
  System.out.println(dayName);
  ```

### Object-Oriented and Procedural Programming (5 marks)
- **Object-Oriented Programming (OOP)**:
  - **Focus**: Objects and classes.
  - **Key Concepts**: Encapsulation, inheritance, polymorphism, abstraction.
  - **Example**:
    ```java
    class Animal {
        void sound() {
            System.out.println("Animal makes a sound");
        }
    }

    class Dog extends Animal {
        void sound() {
            System.out.println("Dog barks");
        }
    }

    public class OOPExample {
        public static void main(String[] args) {
            Animal myDog = new Dog();
            myDog.sound(); // Outputs: Dog barks
        }
    }
    ```

- **Procedural Programming**:
  - **Focus**: Functions and procedures.
  - **Key Concepts**: Sequence of steps or instructions.
  - **Example**:
    ```java
    public class ProceduralExample {
        public static void main(String[] args) {
            printGreeting("World");
        }

        static void printGreeting(String name) {
            System.out.println("Hello, " + name); // Outputs: Hello, World
        }
    }
    ```

Each explanation is concise, focused on the marks allocated, and tailored to fit within the context of Java OOP.

