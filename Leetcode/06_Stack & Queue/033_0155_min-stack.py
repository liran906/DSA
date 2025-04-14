class MinStack:
    
    def __init__(self):
        self.items = []
        self.minstack = []
        

    def push(self, val: int):
        self.items.append(val)
        if len(self.minstack) == 0 or val <= self.minstack[-1]:
            self.minstack.append(val)
        

    def pop(self):
        if len(self.items) == 0:
            return
        top = self.items[-1]
        if len(self.minstack) > 0 and top == self.minstack[-1]:
            self.minstack.pop()
        self.items.pop()
        

    def top(self):
        return self.items[-1]
        

    def getMin(self):
        if len(self.minstack) == 0:
            return
        return self.minstack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()