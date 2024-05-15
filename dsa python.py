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

arr = [[0,0,1,1,1],
       [0,0,1,1,1],
       [0,1,1,1,1]]

print(leetcode(arr))
            
    