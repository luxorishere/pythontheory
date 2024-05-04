def rotate_an_array(ilist, turn):
    rlist = []
    if turn > len(ilist):
        turn = len(ilist) % turn
    
    for i in range(len(ilist) - turn, len(ilist)):
        rlist.append(ilist[i])
    
    for i in range(0, turn + 1):
        rlist.append(ilist[i])
    return rlist

tlist = [1,2,3,4,5]
print(rotate_an_array(tlist, 2))