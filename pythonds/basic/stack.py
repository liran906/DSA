class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def peek(self):
        try:
            return self.items[len(self.items) - 1]
        except:
            return None
    
    def size(self):
        return len(self.items)
    
    def __str__(self):
        out = []
        for i in self.items:
            out.append(i)
        return ' | '.join(out)
    
# # 懒人版5行 stack 实现
# class Stack(list):
#     push = list.append
#     peek = lambda self: self[-1]
#     isEmpty = lambda self: len(self) == 0
#     size = list.__len__