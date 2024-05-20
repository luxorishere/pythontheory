## Java Syllabus

### Unit 1

1. Introduction to Java

Why Java, History of Java, JVM, JRE, Java Environment, Java Source File Structure and Compilation, Fundamental Java Concepts


Why Java:

Java is a high-level, object-oriented programming language that is widely used for developing applications. Java is known for its platform independence, robust security features, and excellent performance. Java is used in a wide range of applications such as web browsers, mobile apps, desktop applications, games, and enterprise software. Java is also used for developing web applications, Android apps, and web services.

History of Java:

Java was first developed by Sun Microsystems, now owned by Oracle Corporation, in 1991. The language was created by James Gosling, Mike Sheridan, and Patrick Naughton. The Java Language was first released in 1995.

JVM:

Java Virtual Machine (JVM) is a software program that runs Java bytecode. JVM is responsible for executing Java code on any device that has a JVM installed. The JVM is platform-independent, which means that Java code can run on any device regardless of the operating system.

JRE:

Java Runtime Environment (JRE) is a software package that includes JVM and additional libraries and tools that are required to run Java applications. JRE is used to run Java applications on a device.

Java Environment:

Java Development Kit (JDK) includes JRE and additional development tools such as a Java compiler, debuggers, and code editors. JDK is used to develop, compile, and run Java applications.

Java Source File Structure and Compilation:

Java source code is written in a text editor or an Integrated Development Environment (IDE). Java source code is saved in a file with a .java extension. The Java compiler (javac) is used to compile Java source code into Java bytecode. The Java bytecode is saved in a file with a .class extension. The JVM executes the Java bytecode to run Java applications.

Fundamental Java Concepts:

Java is an object-oriented language that supports encapsulation, inheritance, and polymorphism. In Java, a class is the blueprint from which objects are created. Objects are instances of classes. A variable is a storage location that holds an object. A method is a block of code that is associated with a class or an object. Java is a statically-typed language, which means that the data type of a variable is determined at compile time. Java is a case-sensitive language, which means that the letters in a variable name must match the case of the letters in the variable declaration.


2. Programming Structures in Java

-  Classes in Java

A class is a blueprint or template for creating objects. A class defines the properties and behaviors of the objects.

A class is defined using the keyword class and it must have a name that starts with a capital letter. The class name is used to create objects.

Here is an example of a class called Person:

```java
class Person {
    // class body
}
```

- Access Specifiers in Java

Access specifiers in Java determine the level of access to the class, its members, or a package. There are four access specifiers in Java: public, private, protected, and default (no modifier).

The access specifier determines who can access the class, its members, or a package.

* **Public**: Public access specifier means that the class, its members, or a package can be accessed from any part of the program as long as it is in the same project or imported.
* **Private**: Private access specifier means that the class, its members, or a package can only be accessed within the same class.
* **Protected**: Protected access specifier means that the class, its members, or a package can be accessed from within the same package or by a subclass in another package. When a class member is marked as protected, it can be accessed by the members of its own class, its subclasses, and classes in the same package.
* **Default**: Default access specifier means that the class, its members, or a package can be accessed from within the same package.

These access specifiers determine the level of access to the class, its members, or a package, and are used to control who can access them.

```java
public class AccessSpecifiers {
    
    // class variables
    public static int publicVar = 10;
    private static int privateVar = 20;
    protected static int protectedVar = 30;
    static int defaultVar = 40;
    
    // constructor
    public AccessSpecifiers() {
        System.out.println("Default constructor");
    }
    
    // public method
    public static void publicMethod() {
        System.out.println("Public method");
    }
    
    // private method
    private static void privateMethod() {
        System.out.println("Private method");
    }
    
    // protected method
    protected static void protectedMethod() {
        System.out.println("Protected method");
    }
    
    // default method
    static void defaultMethod() {
        System.out.println("Default method");
    }
    
    public static void main(String[] args) {
        AccessSpecifiers obj = new AccessSpecifiers();
        
        // accessing public class variable
        System.out.println("Public class variable: " + publicVar);
        
        // accessing private class variable
        // System.out.println("Private class variable: " + privateVar); // COMPILE TIME ERROR
        
        // accessing protected class variable
        System.out.println("Protected class variable: " + protectedVar);
        
        // accessing default class variable
        System.out.println("Default class variable: " + defaultVar);
        
        // accessing public method
        obj.publicMethod();
        
        // accessing private method
        // obj.privateMethod(); // COMPILE TIME ERROR
        
        // accessing protected method
        obj.protectedMethod();
        
        // accessing default method
        obj.defaultMethod();
    }
    
}

/*
Output:

Default constructor
Public class variable: 10
Protected class variable: 30
Default class variable: 40
Public method
Protected method
Default method

*/

```

- Final Keyword

Final keyword is used to prevent the class or variables from getting inherited or modified further in the code.
Final variables are read-only and Final methods are non-overridden.

```java
public class FinalKeyword {
    
    // final variable
    public static final int NUM = 10;
    
    // final method
    public static final void print() {
        System.out.println("Final method");
    }
    
    public static void main(String[] args) {
        // accessing final variable
        System.out.println("Final variable: " + NUM);
        
        // accessing final method
        print();
    }
    
}

```

- Comments

Java supports three types of comments:

- Line comments
- Block comments
- Doc comments

Line comments:

```java
// This is a line comment
```

Block comments:

```java
/*
This is a block comment
*/
```

Doc comments:

```java
/**
 * This is a doc comment
 */
```


- Data types
Data types in Java are divided into two categories:

- Primitive data types
- Non-primitive data types

Primitive data types:

```java
byte
short
int
long
float
double
char
boolean
```

Non-primitive data types:

```java
String
Object
Arrays
Classes
```

- Java Variables

Java variables are used to store data values.

Java variables can be classified as:

- Local variables
- Instance variables
- Class variables

```java

public class LocalInstanceVariables {
    
    // local instance variable
    int x = 10;
    
    void printX() {
        System.out.println(x); // local variable
    }
    
    public static void main(String[] args) {
        LocalInstanceVariables obj = new LocalInstanceVariables();
        obj.printX(); // instance variable
    }
    
}

Class Variables

public class ClassVariables {
    
    // class variable
    static int y = 20;
    
    public static void main(String[] args) {
        int a = 10;
        System.out.println(a); // local variable
        System.out.println(y); // class variable
    }
    
}
```





- Operators

Operators in Java are used to perform mathematical and logical operations.

```java
+ Addition
- Subtraction
* Multiplication
/ Division
% Modulus
++ Increment
-- Decrement


public class Operators {
    public static void main(String[] args) {
        int a = 10;
        int b = 5;
        
        System.out.println(a + b); // addition
        System.out.println(a - b); // subtraction
        System.out.println(a * b); // multiplication
        System.out.println(a / b); // division
        System.out.println(a % b); // modulus
        System.out.println(++a); // increment
        System.out.println(--a); // decrement
    }
    
}

```
- Control Statements

Control statements in Java are used to control the flow of the program.

```java
if-else
switch
for
while
do-while

public class ControlStatements {
    
    public static void main(String[] args) {
        
        int number = 10;
        
        // if else statement
        if(number > 5) {
            System.out.println("Number is greater than 5");
        } else {
            System.out.println("Number is less than or equal to 5");
        }
        
        // switch statement
        switch(number) {
            case 5: 
                System.out.println("Number is 5");
                break;
            case 10:
                System.out.println("Number is 10");
                break;
            default:
                System.out.println("Number is not 5 or 10");
        }
        
        // for loop
        for(int i = 1; i <= 5; i++) {
            System.out.println("Value of i: " + i);
        }
        
        // while loop
        int j = 1;
        while(j <= 5) {
            System.out.println("Value of j: " + j);
            j++;
        }
        
        // do while loop
        int k = 1;
        do {
            System.out.println("Value of k: " + k);
            k++;
        } while(k <= 5);
    }
    
}
```

- Array and String
- Class Inheritance
- Class Variables
- Class Methods
- Class Constructors

3. Object Oriented Programming

- Class and Object 

Why we can't create more than one public class in a single java file?

In Java, you can only have one public class per file and the name of the file should match the name of the public class. This restriction is in place to ensure clear organization and maintainability of code. However, you can have multiple non-public classes in the same file.
- Inheritance
- Subclass and Superclass
- Overriding
- Encapsulation
- Polymorphism
- Interfaces
- Abstraction
- Abstract Classes

4. Packages 

- Defining Packages
- ClassPath Setting for packages
- Making Jar file for packages
- Import and static import naming Convention for Packages


### Unit 3: Java New Features
- Functional Interfaces
- Lambda Expression
- Method References
- Stream API
- Default Methods
- Static Method
- Base64 Encode and Decode
- Decode
- ForEach Method
- Try-with-resources
- Type Annotations
- Repeating Annotations
- Java Module System
- Diamond Syntax with Anonymous Class
- Inner Anonymous Class
- Local Variable Type Inference
- Switch Expressions
- Yield Keyword
- Text Blocks
- Records
- Sealed Classes

### Unit 4: Java Collections Framework
- Collection in Java
- Collection Framework in Java
- Hierarchy of Collection Framework
- Iterator Interface
- Collection Interface
- List Interface
- ArrayList
- LinkedList
- Vector
- Stack
- Queue Interface
- Set Interface
- HashSet
- LinkedHashSet
- SortedSet Interface
- TreeSet
- Map Interface
- HashMap Class
- LinkedHashMap Class
- TreeMap Class
- Hashtable Class
- Sorting
- Comparable Interface
- Comparator Interface
- Properties Class in Java

### Unit 5: Spring Framework and Spring Boot
#### Spring Framework
- Spring Core Basics
- Spring Dependency Injection concepts
- Spring Inversion of Control
- AOP
- Bean Scopes - Singleton
- Prototype
- Request
- Session
- Application
- Web Socket
- Autowiring
- Annotations
- Life Cycle Callbacks
- Bean Configuration styles

#### Spring Boot
- Spring Boot Build Systems
- Spring Boot Code Structure
- Spring Boot Runners
- Logger
- BUILDING RESTFUL WEB SERVICES
- Rest Controller
- Request Mapping
- Request Body
- Path Variable
- Request Parameter
- GET
- POST
- PUT
- DELETE APIs
- Build Web Applications