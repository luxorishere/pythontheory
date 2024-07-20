package javap;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;

public class Class {
    public static void main(String[] args) {
        try{
            FileWriter writer = new FileWriter("javanewfile.txt");
            writer.write("Hello, World!");
            writer.close();
        }
        catch(IOException e){
            e.printStackTrace();
        }
    }
}`
