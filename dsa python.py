def sum_of_array(arr):
    if len(arr) == 1:
        return arr[0]
    
    mid = len(arr) // 2
    left_sum = sum_of_array(arr[:mid])
    right_sum = sum_of_array(arr[mid:])
    
    return left_sum + right_sum

arr = [1, 2, 3, 4, 5]
print(sum_of_array(arr))