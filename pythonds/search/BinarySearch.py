def reBinarySearch(alist, item):
    if len(alist) == 0:
        return False
    else:
        mid = len(alist) // 2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return reBinarySearch(alist[:mid], item)
            else:
                return reBinarySearch(alist[mid+1:], item)

l = [1,2,3,4,5]
print(reBinarySearch(l, 0))
print(reBinarySearch(l, 1))
print(reBinarySearch(l, 4))
print(reBinarySearch(l, 6))

# 没有切片的额外开销
def reBinarySearch(alist, item, start=0, end=None):
    if end is None:
        end = len(alist) - 1
    
    if start > end:
        return False
    else:
        mid = (start + end) // 2
        if alist[mid] == item:
            return True
        else:
            if item < alist[mid]:
                return reBinarySearch(alist, item, start, mid - 1)
            else:
                return reBinarySearch(alist, item, mid + 1, end)

l = [1,2,3,4,5]
print(reBinarySearch(l, 0))
print(reBinarySearch(l, 1))
print(reBinarySearch(l, 5))
print(reBinarySearch(l, 6))