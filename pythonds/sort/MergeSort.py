# def mergeSort(alist, details=False): # details 可以打印细节
#     if len(alist) > 1:
#         # 缩小问题规模，递归调用
#         if details:
#             print('spliting ', alist)
#         mid = len(alist) // 2
#         left = mergeSort(alist[:mid], details)
#         right = mergeSort(alist[mid:], details)

#         # 归并排序
#         if details:
#             print('merging ', left, 'and', right)
#         i, j = 0, 0
#         alist = []
#         while i < len(left) and j < len(right):
#             if left[i] < right[j]:
#                 alist.append(left[i])
#                 i += 1
#             else:
#                 alist.append(right[j])
#                 j += 1
        
#         # 下面用切片也行，但会增加空间复杂度
#         while i < len(left):
#             alist.append(left[i])
#             i += 1
#         while j < len(right):
#             alist.append(right[j])
#             j += 1
    
#     return alist

def mergeSort(alist, details=False):
    if len(alist) > 1:
        # 缩小问题规模，递归调用
        if details:
            print('splitting   :', alist)
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]
        mergeSort(left, details)
        mergeSort(right, details)

        # 归并排序
        if details:
            print('merging     :', left, 'and', right)
        i, j, k = 0, 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1
            k += 1

        # 合并剩余的元素
        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1
        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1

        if details:
            print('after merge :', alist)

    return alist


if __name__ == '__main__':
    l = [2, 8, 7, 1, 9, 3, 5, 0, 4, 3, 1]
    print('Sorted list :', mergeSort(l, True))