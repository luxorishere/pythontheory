def leetcode(string):
    ilist = [];
    for i in range(0, len(string)):
        ilist.append(string[i])
    return ilist
def solution(string):
    ilist = leetcode(string)
    maxlen = 0
    templist = []
    rlist = []
    i = 0
    temp = 0
    for i in range(0, len(ilist)):
        temp = 1
        templist = []
        templist.append(ilist[i])
        for j in range(i + 1, len(ilist)):
            if ilist[i] == ilist[j]:
                break
            else:
                templist.append(ilist[j])
                temp += 1
            
        if maxlen < temp:
            maxlen = temp
            rlist = templist
        
    return rlist
        

print(solution("abcabcbb"))