package javatemp;

import java.util.Arrays;

class javatemp{
    public static void main(String[] args) {
        String str = "Hello";
        System.out.println(swap(str));
        
    } 
    static String swap(String str){
        char[] array = str.toCharArray();

        int start = 0;
        int end = str.length() - 1;
        while (start <= end){
            char temp = array[start];
            array[start] = array[end];
            array[end] = temp;
        }
        return array.toString();
    }  
   
    


}