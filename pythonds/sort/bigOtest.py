import time
from random import randint
from BubbleSort import bubbleSort
from SelectionSort import selectionSort
from InsertSort import insertionSort
from ShellSort import shellSort
from MergeSort import mergeSort
from QuickSort import quickSort
from RadixSort import radixSort
from HeapSort import heapSort

def test_sort(sort_function, data, name):
    l = data[:]  # 深拷贝，避免修改原数据
    t1 = time.perf_counter()
    out = sort_function(l)
    t2 = time.perf_counter()
    if not all(out[i] <= out[i+1] for i in range(len(out)-1)):  # 验证排序正确性
        print(f"Error: {name} did not sort the list correctly.")
    print(f'{name} {(t2 - t1):.6f} seconds')

# 生成数据
short_lst = [randint(0, 10000) for _ in range(10000)]  # 10,000 个随机数
lst = [randint(0, 10000) for _ in range(100000)]       # 100,000 个随机数
print(f'Test begin: short list = {len(short_lst)} numbers, full list = {len(lst)} numbers.')

# 测试 O(n²) 排序算法
test_sort(bubbleSort, short_lst, 'bubble sort (10,000 items)')
test_sort(selectionSort, short_lst, 'selection sort (10,000 items)')
test_sort(insertionSort, short_lst, 'insertion sort (10,000 items)')

# 测试高效排序算法
test_sort(shellSort, lst, 'shell sort (100,000 items)')
test_sort(mergeSort, lst, 'merge sort (100,000 items)')
test_sort(quickSort, lst, 'quick sort (100,000 items)')
test_sort(radixSort, lst, 'radix sort (100,000 items)')
test_sort(heapSort, lst, 'heap sort (100,000 items)')