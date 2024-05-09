package javap;
public class javaclass{
    public int a = 1;
    public static int b = 2;


    public static void main(String[] args) {
        Student s1 = new Student("Parth", 1);
        s1.info();
        System.out.println(b);
        
    }
}
class Student{
    String name;
    int id;


    public Student(String name, int id){
        this.name = name;
        this.id = id;
    }
    public void info(){
        System.out.println(this.name + " " + this.id);
    }
}