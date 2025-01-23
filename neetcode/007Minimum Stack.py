# Minimum Stack
# https://neetcode.io/problems/minimum-stack
# med

class MinStack:
    def __init__(self):
        self.items = []
        self.minRecordList = []
        
    def push(self, val: int):
        self.items.append(val)
        if self.minRecordList:
            minVal = min(self.minRecordList[-1], val)
        else:
            minVal = val
        self.minRecordList.append(minVal)
        
    def pop(self):
        self.items.pop()
        self.minRecordList.pop()
        
    def top(self):
        return self.items[-1]

    def getMin(self):
        return self.minRecordList[-1]