def finding_the_missing(ilist, k):
    if check(ilist) == True:
        return ilist[len(ilist) - 1] + k
        
    limit = ilist[len(ilist) - 1]
    tlist = []
    for i in range(1, limit + 1):
        tlist.append(i)
        
    rlist = []
    t = 0
    tcounter = 0
    icount = 0
    while t != k:
        if tcounter < len(tlist) - 1 and tlist[tcounter] not in ilist:
            icount = tlist[tcounter]
            t += 1
        elif tcounter >= len(tlist):
            icount = 0
            icount = ilist[len(ilist) - 1] + k - t
            break
        tcounter += 1

    return icount
def check(ilist):
    if len(ilist) == 1:
        return True
    for i in range(0, len(ilist) - 1):
        if ilist[i] - ilist[i - 1] > 1:
            return False
    return True
