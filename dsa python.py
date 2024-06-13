# max time number comes

def max_time_number_comes(arr):
    i = 1
    count = 1
    first = arr[i]
    while (i < len(arr)):
        if count == 0:
            first = arr[i]
            count = 1
        elif arr[i] == first:
            count += 1
        else:
            count -= 1
        i += 1
    return first

arr = [2,2,2,3,2,3,2,3]
print(max_time_number_comes(arr))