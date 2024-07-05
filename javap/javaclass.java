package javap;

public class javaclass {
    public static void main(String[] args) {
        int result = calculate(5, 3, '+');
        System.out.println(result);
    }

    static int calculate(int num1, int num2, char operator) {
        switch (operator) {
            case '+':
                return num1 + num2;
            case '-':
                return num1 - num2;
            case '*':
                return num1 * num2;
            case '/':
                if (num2 != 0) {
                    return num1 / num2;
                } else {
                    throw new ArithmeticException("Division by zero");
                }
            default:
                throw new IllegalArgumentException("Invalid operator");
        }
    }

    static void fun(int n) {
        if (n == 0) {
            return;
        }
        System.out.println(n);
        n -= 1;

        fun(n);
    }
}
