def insertionSort(alist):
    for i in range(1, len(alist)):
        for j in range(i):
            if alist[i] < alist[j]:
                alist.insert(j, alist.pop(i))
    return alist

# 每次 insert 或 pop 都需要对后续元素重新排序，导致性能低于标准实现


def insertionSort(alist):
    for i in range(1, len(alist)):
        currentValue = alist[i]
        index = i

        # 比较 前一个数据项（index-1）和需要插入值 currentValue 的大小
        while index > 0 and alist[index - 1] > currentValue:
            alist[index] = alist[index - 1]
            index -= 1
        # 插入值放到第一个比他小的数据项（index-1）的前面（index）
        alist[index] = currentValue
    return alist

if __name__ == '__main__':
    l = [2,5,4,3,0,8,4,9,7,6]
    print(insertionSort(l))