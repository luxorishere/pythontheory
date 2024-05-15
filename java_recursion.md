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
### Revering the number
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
