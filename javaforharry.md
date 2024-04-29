```java
package com.javapackage;
public class Human {
        public static void main(String[] args) {

            Student s = new Student("Parth", 20);
            Student s1 = new Student("Harshit", 20);
            Student s2 = new Student(20);
            Student s3 = new Student();

            System.out.println(s.name + " ");
            System.out.println(s1.name + " " + s1.age);
            System.out.println(" " + s2.age);
            System.out.println(s3.name + " " + s3.age);




        }

}
class Student{
    String name;
    int age;

    Student (String name, int age){
        this.name = name;
        this.age = age;
    }
    Student(String name){
        this.name = name;

    }
    Student(int age){
        this.name = "Parth";
        this.age = age;
    }
    Student(){
        System.out.println("Please enter the value");
    }




}

```