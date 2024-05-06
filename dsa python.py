import pandas as pd

def leetcode(arr, target):
    arr2d = []
    templ = []
    i = 0
    sum = 0 
    while i < len(arr):
        temp = sum + arr[i]
        if temp <= target:
            sum += arr[i]
            templ.append(arr[i])
            if True:
                arr2d.append(templ)
                
            
            
            
        else:
            i += 1
        
        if sum == target:
            return templ
    return [[-1,-1]]

arr = [2,3,5]
print(leetcode(arr,11))
            
            
            
        