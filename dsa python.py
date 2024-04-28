def leetcode(ilist, account):
    sum = 0
    i = len(ilist) - 1
    count = 0
    if account < ilist[i]:
        return 0
    while sum != account or i != 0:
        temp = sum
        temp += ilist[i]
        if temp <=  account: 
            
            sum += ilist[i]
            count += 1
            
        else:
            i -= 1
    while account != sum:
        ilist.pop()
        leetcode(ilist, account)
        
        
    if count != 0:
        return count
    else:
        return -1

print(leetcode([2,3,5], 11))
        
            
        