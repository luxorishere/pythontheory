# DSA Python 

### Number of One from right side
```python
def leetcode(array):
    rstart = 0
    rend = len(array)
    cstart = 0
    cend = len(array[0]) - 1
    count = 0
    temp = 0
    while rstart < rend:
        if cend > -1 and array[rstart][cend] == 1:
            count += 1
            cend -= 1
            if temp > count:
                continue
            else:
                temp = count
        else:
            rstart += 1
            count = 0
            cend = len(array[0]) - 1
       
    return temp
```
### Print the elements of matrix in sorted manner

```python
def leetcode_matrix(array):
    arr = []
    for i in range(0, len(array)):
        for j in range(0, len(array[0])):
            arr.append(array[i][j])
    arr.sort()
    count = 0
    for i in range(0 , len(array) * len(array[0])):
        if count == len(array[0]):
            print("\n")
            count = 0
        print(f"{arr[i] }")
        count += 1

```