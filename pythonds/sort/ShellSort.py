def shellSort(alist):
    sublistCount = len(alist) // 2
    while sublistCount > 0:
        for start in range(sublistCount):
            gapInsertionSort(alist, start, sublistCount)
        sublistCount = sublistCount // 2
    return alist

def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentValue = alist[i]
        index = i
        while index > 0 and alist[index-gap] > currentValue:
            alist[index] = alist[index-gap]
            index -= gap
        alist[index] = currentValue

if __name__ == '__main__':
    l = [2,5,4,3,0,8,4,9,7,6]
    print(shellSort(l))