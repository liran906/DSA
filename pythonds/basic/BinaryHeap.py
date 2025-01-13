class BinaryHeap:
    def __init__(self, lst=None):
        self.heapLst = [None]
        self.heapSize = 0
        if lst:
            self.buildHeap(lst)
    
    def swap(self, i_1, i_2):
        self.heapLst[i_1], self.heapLst[i_2] = self.heapLst[i_2], self.heapLst[i_1]

    def insert(self, item):
        self.heapLst.append(item)
        self.heapSize += 1
        itemIndex = self.heapSize
        self.percolateUp(itemIndex) # 向上排序
    
    def percolateUp(self, index):
        while self.heapLst[index//2] is not None and self.heapLst[index] < self.heapLst[index//2]:
            self.swap(index, index // 2)
            index = index // 2

    def findMin(self):
        if self.heapSize:
            return self.heapLst[1]
        raise ValueError('Empty heap.')
    
    def delMin(self):
        if self.heapSize == 0:
            raise IndexError('Empty heap.')
        minVal = self.findMin()
        self.heapLst[1] = self.heapLst[self.heapSize]
        self.heapLst.pop()
        self.heapSize -= 1
        self.percolateDown(1) # 从根向下排序
        
        return minVal
    
    def percolateDown(self, index):
        while index * 2 <= self.heapSize:
            minChildIndex = index * 2 # assume left child is min
            if minChildIndex + 1 <= self.heapSize and self.heapLst[minChildIndex] > self.heapLst[minChildIndex+1]:
                minChildIndex += 1 # right child exisits and is min
            if self.heapLst[index] > self.heapLst[minChildIndex]:
                self.swap(index, minChildIndex)
                index = minChildIndex
            else:
                break
    
    def isEmpty(self):
        return self.heapSize == 0
    
    def size(self):
        return self.heapSize
    
    def buildHeap(self, alist):
        self.heapSize = len(alist)
        self.heapLst.extend(alist)
        itemIndex = self.heapSize // 2 # 从最后一个节点的父节点开始
        while itemIndex > 0:
            self.percolateDown(itemIndex)
            itemIndex -= 1

if __name__ == '__main__':
    # Test script for the BinaryHeap class
    def test_binary_heap():
        print("=== Testing BinaryHeap ===")
        
        # Create a new binary heap
        heap = BinaryHeap()
        print("Empty heap created.")
        
        # Test inserting elements
        elements = [10, 4, 9, 1, 7, 5, 3]
        for el in elements:
            heap.insert(el)
            print(f"Inserted {el}, current heap: {heap.heapLst[1:]}")
        
        # Check the minimum element
        min_val = heap.findMin()
        print(f"Minimum value in the heap: {min_val}")
        assert min_val == 1, "Test failed: The minimum value should be 1."

        # Remove the minimum element
        removed = heap.delMin()
        print(f"Removed minimum value: {removed}, current heap: {heap.heapLst[1:]}")
        assert removed == 1, "Test failed: The removed value should be 1."

        # Test heap after removal
        print(f"Heap after removing the minimum: {heap.heapLst[1:]}")
        
        # Build a heap from a list
        initial_list = [9, 5, 6, 2, 3]
        heap2 = BinaryHeap(initial_list)
        print(f"Heap built from {initial_list}: {heap2.heapLst[1:]}")
        
        # Ensure the minimum value is correct
        assert heap2.findMin() == 2, "Test failed: The minimum value should be 2."

        # Remove elements one by one
        while not heap2.isEmpty():
            print(f"Removed {heap2.delMin()}, remaining heap: {heap2.heapLst[1:]}")
        
        print("All tests passed!")

    # Run the test
    test_binary_heap()