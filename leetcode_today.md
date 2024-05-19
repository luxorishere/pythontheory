1. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/description/

2. Largest Sum Contiguous Subarray (Kadane’s Algorithm)
https://leetcode.com/problems/maximum-subarray/description/

3. Score of a String
https://leetcode.com/problems/score-of-a-string/description/

### Doubts

```java
static int[] recursion(int[] arr, int start, int end){
        if (start == end){
            return new int[] {arr[start], arr[end]};
        }
        if (start + 1 == end){
            return new int[] {Math.max(arr[start], arr[end]), Math.min(arr[start], arr[end])};
        }
        int mid = (start + end) / 2;

        int[] left = recursion(arr,start, mid);
        int[] right = recursion(arr, mid, end);

        int overallmax = Math.max(left[0], right[0]);
        int overallmin = Math.min(left[1], right[1]);

        return new int[] {overallmax, overallmin};

    }
    static int[] max(int[] arr){
        int max = Integer.MIN_VALUE;
        for (int j : arr) {
            max = Math.max(max, j);

        }
        int min = Integer.MAX_VALUE;
        for (int j : arr) {
            min = Math.min(min, j);
        }
        return new int[] {max, min};

    }

```