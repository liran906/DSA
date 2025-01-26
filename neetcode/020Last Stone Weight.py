# Last Stone Weight
# https://neetcode.io/problems/last-stone-weight
# e

class Maxheap:
    def __init__(self, lst=None):
        self.items = [None]
        if lst:
            self.build(lst)
    
    def build(self, lst):
        for i in lst:
            self.push(i)
    
    def swap(self, i1, i2):
        self.items[i1], self.items[i2] = self.items[i2], self.items[i1]
    
    def push(self, item):
        if self.items == [None]:
            self.items.append(item)
        else:
            self.items.append(item)
            index = len(self.items) - 1
            while index >= 2 and self.items[index] > self.items[index // 2]:
                self.swap(index, index // 2)
                index = index // 2
    
    def getmax(self):
        if self.items == [None]:
            return None
        return self.items[1]
    
    def popmax(self):
        if len(self.items) == 1:
            raise ValueError
        if len(self.items) == 2:
            return self.items.pop()
        else:
            popitem = self.items[1]
            self.items[1] = self.items.pop()
            index = 1
            while index * 2 < len(self.items):
                maxIndex = index * 2
                if maxIndex + 1 < len(self.items) and self.items[maxIndex] < self.items[maxIndex + 1]:
                    maxIndex += 1
                if self.items[index] < self.items[maxIndex]:
                    self.swap(index, maxIndex)
                    index = maxIndex
                else:
                    break
            return popitem

class Solution:
    def lastStoneWeight(self, stones):
        if len(stones) == 1:
            return stones[0]
        
        mh = Maxheap(stones)
        while len(mh.items) >= 3:
            s1 = mh.popmax()
            s2 = mh.popmax()
            if s1 > s2:
                mh.push(s1 - s2)
        if len(mh.items) == 2:
            return mh.getmax()
        else:
            return 0
        
s = Solution()
print(s.lastStoneWeight([2,3,6,2,4]))