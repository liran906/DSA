def selectionSort(alist):
    for fillslot in range(len(alist) - 1, 0, -1):
        maxPos = 0
        for i in range(1, fillslot + 1): # max从 0 开始，所以range 从 1 开始，少一次比对
            if alist[i] > alist[maxPos]:
                maxPos = i
        temp = alist[fillslot]
        alist[fillslot] = alist[maxPos]
        alist[maxPos] = temp
    return alist

if __name__ == '__main__':
    l = [2,8,7,1,9,3,5,0,4,3,1]
    print(selectionSort(l))
    print(l)