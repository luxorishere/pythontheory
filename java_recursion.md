# Java Recurison

### Check Palindrome number or not

```java
 static boolean recursion(int number, int temp, int check){
        if (number == 0){
            return temp == check;
        }
        temp = (temp * 10) + number % 10;
        return recursion(number / 10, temp, check);
    }
```
### Reversing the number
```java
static int reverse(int num){
        int digit = (int)Math.log10(num) + 1;
        return helper(num , digit);


    }
    static int helper(int num, int digits){
        if (num % 10 == num){
            return num;
        }
        return num % 10 * (int)Math.pow(10 , digits - 1) + helper(num / 10, digits - 1);
    }
```
### Checking the number of zeroes

```java
static int zeroes(int number, int count){
        if (number == 0){
            return count;
        }
        int temp = number % 10;
        if (temp == 0){
            count += 1;
        }
        return zeroes(number / 10, count);
    }
```
### Check array is sorted or not

```java
static boolean check(int[] arr, boolean test, int i){
        if (i == arr.length - 1){
            return test;
        }
        if (arr[i] > arr[i + 1]){
            return false;
        }

        return check(arr,test, i + 1);
    }
    
```
```java
 static boolean array_check(int[] arr){
        if (arr.length <= 1){
            return true;
        }
        return arr[0] <= arr[1] && array_check(Arrays.copyOfRange(arr,1,arr.length - 1));
    }
```
```java
static boolean array_check(int[] arr, int index){
        if (index == arr.length -1 ){
            return true;
        }
        return arr[index] <= arr[index + 1] && array_check(arr, index + 1);
    }
```
### Binary Search

```java
static int binary_search(int[] arr, int target,int start, int end){
        if (start > end){
            return -1;
        }
        int mid = (start + end) / 2;
        if (arr[mid] == target){
            return mid;
        }
        else if (arr[mid] > target){
            return binary_search(arr, target, start, mid);
        }
        else{
            return binary_search(arr, target, mid + 1, end);
        }
    }
```

```java
static int linear_search(int[] arr, int target, int index){
        if (index > arr.length - 1){
            return -1;
        }
        if (arr[index] == target){
            return index;
        }
        return linear_search(arr,target, index + 1);
    }
    static boolean linear_check_boolean(int[] arr, int target, int index){
        if (index > arr.length - 1){
            return false;
        }
        return arr[index] == target || linear_check_boolean(arr,target, index + 1);
    }
```
### Adding in the Arraylist 

```java
static ArrayList<Integer> list = new ArrayList<>();
    static void linear_check_boolean(int[] arr, int target, int index){
        if (index > arr.length - 1){
            return;
        }
        if (arr[index] == target){
            list.add(index);
        }
        linear_check_boolean(arr, target, index + 1);
    }
```
```java
static ArrayList linear_check_boolean(int[] arr, int target, int index, ArrayList<Integer> list){
        if (index > arr.length - 1){
            return list;
        }
        if (arr[index] == target){
            list.add(index);
        }
        return linear_check_boolean(arr, target, index + 1, list);

    }
```

### Recursion and linear search without passing the argument

