def sequentialSearch(alist, item):
    i = 0
    found = False

    while i < len(alist) and not found:
        if alist[i] == item:
            found = True
        else:
            i += 1
    return found

l = [1,2,3,4,5]
print(sequentialSearch(l, 1))
print(sequentialSearch(l, 5))
print(sequentialSearch(l, 6))

# 顺序查找有序表，可能可以提前结束
def orderedSequentialSearch(alist, item):
    i = 0
    found = False
    stop = False

    while i < len(alist) and not found and not stop:
        if alist[i] == item:
            found = True
        else:
            if alist[i] > item:
                stop = True
            else:
                i += 1
    return found