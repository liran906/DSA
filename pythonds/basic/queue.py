class Queue():
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return self.items == []
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        return self.items.pop(0)
    
    def size(self):
        return len(self.items)

# # 简洁版
# class Queue(list):
#     enqueue = list.append
#     dequeue = lambda self: self.pop(0)
#     isEmpty = lambda self: len(self) == 0
#     size = list.__len__