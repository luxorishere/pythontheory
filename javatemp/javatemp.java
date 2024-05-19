
package javatemp;
import java.util.Scanner;
public class javatemp {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.println("Enter the Year");
        int year = input.nextInt();
        System.out.println("Enter the total year");
        int total_year = input.nextInt();
        if (total_year - year <= 1){
            System.out.println("Yes you are de sakte ho");
        }
        else{
            System.out.println("Nahi de sakte");
        }
    }
    
}
