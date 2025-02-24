def matchResistors(R,n):
    # init
    d = {}
    for r in R:
        d[r] = d.get(r, 0) + 1
    res = []
    
    # trasversal
    for i in range(len(R)):
        r1, r2 = R[i], n - R[i]
        
        if r2 in d and d[r1] > 0 and d[r2] > 0:
            # r1 & r2 are the same
            if r1 == r2 and d[r1] > 1:
                res.append((r1, r1))
                d[r1] -= 2
            
            # r1 & r2 are not the same
            elif r1 != r2:
                res.append((r1, r2))
                d[r1] -= 1
                d[r2] -= 1
    return res

xx = [3,10,4,10,5,6,10,7,8,10,11,9,3,3,10,10,10]
print(matchResistors(xx, 20))

from random import shuffle
longlist = [i for i in range(1,10000)]
shuffle(longlist)
print(len(matchResistors(longlist,10000)))