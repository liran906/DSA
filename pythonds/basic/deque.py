class Deque:
    def __init__(self):
        self.items = []
    
    # 与队列相似，首端和尾端可以对调，则时间复杂度也会对调。
    def addFront(self, item):
        self.items.insert(0, item)
    
    def addRear(self, item):
        self.items.append(item)
    
    def removeFront(self):
        return self.items.pop(0)
    
    def removeRear(self):
        return self.items.pop()
    
    def isEmpty(self):
        return self.items == []
    
    def size(self):
        return len(self.items)