
from sys import maxsize
def square(num):
    ilist = []
    for i in range(1, num + 1):
        if i * i <= num:
            ilist.append(i * i)
        else:
            break
    return ilist
def leetcode(ilist, target):
    start = 0
    end = len(ilist) - 1
    if ilist[end] <= target:
        count = 1
        sum = ilist[end]
    else:
        count = 0
        sum = ilist[end]

    while start <= end:
        
        if sum + ilist[end] == target:
            count += 1
            return count
        elif sum + ilist[end] > target:
            end -= 1
        else:
            count += 1
            sum +=  ilist[end]
    return count
    
def leetcode_list(ilist, target):
    minimum = maxsize
    
    while len(ilist) > 0:
        minimum = min(minimum, leetcode(ilist, target))
        ilist.pop()
    return minimum
        


ilist = square(43)
print(ilist)
print(leetcode_list(ilist,43))