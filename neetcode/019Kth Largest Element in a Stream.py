# Kth Largest Element in a Stream
# https://neetcode.io/problems/kth-largest-integer-in-a-stream
# e

# The Minheap class is particularly for this problem, missing lots of Minheap funtions.
class Minheap:
    def __init__(self, list):
        self.items = [None] + list
    
    def push(self, item):
        self.items.append(item)
        index = len(self.items) - 1
        while index >= 2 and self.items[index] < self.items[index // 2]:
            self.items[index], self.items[index // 2] = self.items[index // 2], self.items[index]
            index = index // 2
    
    def getmin(self):
        if len(self.items) > 1:
            return self.items[1]
    
    def popmin(self):
        if len(self.items) <= 1:
            raise IndexError
        elif len(self.items) == 2:
            self.items.pop()
        else:
            self.items[1] = self.items.pop()
            index = 1
            while index * 2 < len(self.items):
                minIndex = index * 2
                if minIndex + 1 < len(self.items) and self.items[minIndex+1] < self.items[minIndex]:
                    minIndex += 1
                if self.items[index] > self.items[minIndex]:
                    self.items[index], self.items[minIndex] = self.items[minIndex], self.items[index]
                    index = minIndex
                else:
                    break

class KthLargest:
    def __init__(self, k, nums):
        self.k = k
        if nums:
            nums = sorted(nums)
        if k < len(nums):
            nums = nums[len(nums)-k:]
        self.mh = Minheap(nums)

    def add(self, val):
        self.mh.push(val)
        while len(self.mh.items) - 1 > self.k:
            self.mh.popmin()
        return self.mh.getmin()

t = KthLargest(3, [1000, -1000])
print(t.add(0))
print(t.add(2))
print(t.add(-3))
print(t.add(1000))