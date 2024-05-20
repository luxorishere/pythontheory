import numpy as np
def leetcode(arr):
    ilist = []
    rstart = 0
    rend = len(arr)
    temp = 0
    while temp != rend:
        ilist = []
        rend = len(arr)
        rstart = 0
        while rstart <= rend - 1:  # Fixed index out of range error
        
            if rstart < rend - 1 and arr[rstart][1] >= arr[rstart + 1][0] and arr[rstart]:
                minimum = min(arr[rstart][0], arr[rstart + 1][0])
                maximum = max(arr[rstart][1], arr[rstart + 1][1])
                ilist.append([minimum, maximum])
                rstart += 1
            else:
                ilist.append([arr[rstart][0], arr[rstart][1]])
            rstart += 1
        arr = np.copy(ilist)
        temp += 1
    
    # Append the last interval
            
    return ilist

arr =[[1,4],[0,0]]
print(leetcode(arr))
