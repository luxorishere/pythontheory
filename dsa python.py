from numpy import sort


def char_to_ascii(s):
    return ord(s)
def ascii_to_char(num):
    return chr(num)

def charleetcode(ilist):
    numlist = []
    for i in ilist:
        numlist.append(char_to_ascii(i))
    return numlist

def leetcode(ilist, chartarget):
    numlist = charleetcode(ilist)
    target = char_to_ascii(chartarget)
    numlist = sort(numlist)
    for i in range(0, len(ilist)):
        temp = numlist[i] - target
        if temp > 0:
            return ascii_to_char(numlist[i])
        
        
    return -1
        
        
rlist = ["c", "d", "e"]
target = "a"
print(leetcode(rlist, target))