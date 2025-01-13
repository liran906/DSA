import sys
sys.path.append('.')
from pythonds.basic.BinaryHeap import BinaryHeap

def heapSort(alist):
    heap = BinaryHeap(alist)
    i = 0
    while not heap.isEmpty():
        alist[i] = heap.delMin()
        i += 1
    return alist

if __name__ == '__main__':
    l = [2,5,4,3,0,8,4,9,7,6]
    print(heapSort(l))