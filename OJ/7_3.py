initLst = [int(_) for _ in input().split()]
middLst = [int(_) for _ in input().split()]

# in_ = '3 1 2 8 7 5 9 4 0 6'
# mi_ = '1 3 2 8 5 7 4 9 0 6'
# initLst = [int(_) for _ in in_.split()]
# middLst = [int(_) for _ in mi_.split()]

def insertionSort(alist):
    recordLayer_i = []
    for i in range(1, len(alist)):
        current = alist[i]
        index = i
        while index > 0 and alist[index - 1] > current:
            alist[index] = alist[index - 1]
            index -= 1
        alist[index] = current
        if recordLayer_i == middLst: # 判断上次list是否等于给定list
            return True, [str(_) for _ in alist]
        recordLayer_i = alist[:]
    return False, alist

recordLayer_m = []
found = 0

def mergeSort(alist, gap=2):
    global found, recordLayer_m
    if alist == middLst:
        found = 1
    
    thisLayer = []
    for i in range(len(alist)):
        if i % gap == 0:
            merged = [alist[i]]
        elif i % gap == gap - 1:
            merged.append(alist[i])
            for item in sorted(merged):
                thisLayer.append(item)
            merged = []
        else:
            merged.append(alist[i])
    
    if merged:
        for item in sorted(merged):
            thisLayer.append(item)
    
    if gap >= len(alist):
        return thisLayer
    else:
        gap *= 2
        if found == 1:
            recordLayer_m = [str(_) for _ in thisLayer]
            found = 2
        return mergeSort(thisLayer, gap)

ibo, ilst = insertionSort(initLst[:])
mergeSort(initLst)

if ibo == True:
    print('Insertion Sort')
    print(' '.join(ilst))
else:
    print('Merge Sort')
    print(' '.join(recordLayer_m))



# l = [1,4,3,7,5,3,2,8,5,9,0,2,5]
# print(l)
# out = insertionSort(l)
# for i in recordLayer_i:
#     print(i)
# print(out)