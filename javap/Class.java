package javap;

public class Class{
    public static void main(String[] args) {
        int[] arr = {10,0,1};
        System.out.println(water_tank(arr));

    }
    static int water_tank(int[] arr){
        int sum = 0;
        int result = 0;
        for (int i = 0; i < arr.length; i++) {
            sum = 0;
            for (int j = i + 1; j < arr.length - 1; j++) {
                if (arr[j] >= arr[i]){
                    continue;
                }
                else{
                    int dif = arr[i] - arr[j];
                    sum += dif;
                }
                result = Math.max(sum, result);

                
            }
            
        }
        return result;
    }
}