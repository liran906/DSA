def quickSort(alist, start=0, end=None):
    if end is None:
        end = len(alist) - 1
    
    if start > end:
        return alist
    else:
        mid = alist[start]
        lmark = start + 1
        rmark = end
        while lmark < rmark:
            # 增加左右标直到超过 mid
            while lmark < rmark and alist[lmark] < mid:
                lmark += 1
            while lmark <= rmark and alist[rmark] > mid:
                rmark -= 1
            # 互换
            if lmark < rmark:
                temp = alist[rmark]
                alist[rmark] = alist[lmark]
                alist[lmark] = temp
        # 右标与中值mid互换
        alist[start] = alist[rmark]
        alist[rmark] = mid
        quickSort(alist, start, rmark - 1)
        quickSort(alist, rmark + 1, end)
        return alist

def quickSort(alist, start=0, end=None):
    if end is None:
        end = len(alist) - 1

    if start >= end:  # 基础条件：数组长度为0或1
        return
    
    mid = alist[start]  # 基准值
    lmark = start + 1
    rmark = end

    while lmark <= rmark:  # 注意这里为 <= 而不是 <，确保所有元素都处理
        while lmark <= rmark and alist[lmark] < mid:  # 找到左侧不小于基准值的元素
            lmark += 1
        while lmark <= rmark and alist[rmark] > mid:  # 找到右侧不大于基准值的元素
            rmark -= 1
        if lmark <= rmark:  # 左右标记未交错，交换
            alist[lmark], alist[rmark] = alist[rmark], alist[lmark]
            lmark += 1
            rmark -= 1

    # 将基准值放到正确位置，由于左右两部分仅仅是和 mid 值大小的比较，并没有排序
    # 所以将rmark换到start或者其他以左的位置都没问题
    alist[start], alist[rmark] = alist[rmark], alist[start]

    # 递归处理左右子数组
    quickSort(alist, start, rmark - 1)
    quickSort(alist, rmark + 1, end)

    return alist

if __name__ == '__main__':
    l = [1,5,3,3,3,0,4,2]
    print(quickSort(l))
    print((l))