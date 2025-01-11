from node import Node

class DoublyLinkedList():
    def __init__(self, it = None):
        self.head = None
        self.tail = None
        self.lenth = 0 # 维护一个长度，size可以O(1)
        if it is not None: # 初始化的时候，直接导入一个现有的可迭代对象
            for d in it:
                self.append(d)
    
    def isEmpty(self):
        return not self.head
    
    def add(self, item):
        newNode = Node(item)
        newNode.next = self.head
        if self.head:
            self.head.prev = newNode # 如果是空表，则没有这一步
        else:
            self.tail = newNode # 如果是空表，尾节点设为这个节点
        self.head = newNode
    
    def search(self, item):
        currentNode = self.head
        while currentNode:
            if currentNode.getData() == item:
                return True
            currentNode = currentNode.next
        return False
    
    def size(self):
        return self.lenth # 用上了新维护的lenth属性

    __len__ = size # 定义魔术方法 __len__
    
    def remove(self, item):
        currentNode = self.head
        while currentNode:
            if currentNode.getData() == item:
                currentNode.prev.next = currentNode.next
                currentNode.next.prev = currentNode.prev
                return True # 删除成功返回 true，反之返回 false
            currentNode = currentNode.next
        return False
    
    # 用尾结点：
    def append(self, item):
        newNode = Node(item)
        newNode.prev = self.tail
        if self.tail:
            self.tail.next = newNode # 非空表
        else:
            self.head = newNode # 空表
        self.tail = newNode
    
    def index(self, item):
        currentNode = self.head
        counter = 0
        while currentNode:
            if currentNode.getData() == item:
                return counter
            currentNode = currentNode.next
            counter += 1
        return None
    
    def pop(self, pos = -1):
        currentNode = self.head
        counter = 0
        if pos == 0:
            self.head = currentNode.next
            currentNode.next.prev = None
            return currentNode.getData()
        elif pos == -1:
            currentNode = self.tail # 直接等于尾结点
            self.tail = currentNode.prev
            currentNode.prev.next = None
            return currentNode.getData()
        else:
            while counter != pos:
                currentNode = currentNode.next
                counter += 1
            currentNode.next.prev = currentNode.prev
            currentNode.prev.next = currentNode.next
            return currentNode.getData()
    
    def insert(self, pos, item):
        if pos == 0:
            self.add(item)
        elif pos == self.size() - 1:
            self.append(item)
        else:
            newNode = Node(item)
            currentNode = self.head
            counter = 0
            while counter != pos:
                currentNode = currentNode.next
                counter += 1
            newNode.next = currentNode
            newNode.prev = currentNode.prev
            currentNode.prev.next = newNode
            currentNode.prev = newNode
    
    def getTail(self):
        return self.tail
    
    def __getitem__(self, index):
        counter = 0
        if isinstance(index, slice):
            start = 0 if index.start is None else index.start # 严谨的写法，余同
            stop = self.size() if index.stop is None else index.stop
            step = 1 if index.step is None else index.step
            # start = index.start or 0
            # stop = index.stop or self.size()
            # step = index.step or 1
            currentNode = self.head if step > 0 else self.tail # 考虑负数步长
            counter = 0 if step > 0 else self.size() # 考虑负数步长
            stepCounter = 0
            outLst = DoublyLinkedList() # 切片对象也应该是双链表
            if step > 0:
                while counter < start: # 遍历直到start
                    currentNode = currentNode.getNext()
                    counter += 1
                while counter < stop: # 只能用小于，以防 step 过大
                    # currentNode = currentNode.next # 其实区别不大，换下面写法也行
                    # counter += 1
                    # stepCounter += 1
                    # if stepCounter % step == 0:
                    #     outLst.append(currentNode.getData())
                    outLst.append(currentNode.getData())
                    stepCounter = step
                    while currentNode is not None and stepCounter > 0:
                        currentNode = currentNode.getNext()
                        stepCounter -= 1
                    counter += step
            elif step < 0:
                while counter > stop:
                    currentNode = currentNode.getPrev()
                    counter -= 1
                while counter > start:
                    outLst.append(currentNode.getData())
                    stepCounter = -step # stepcounter 取正
                    while currentNode is not None and stepCounter > 0:
                        currentNode = currentNode.getPrev()
                        stepCounter -= 1
                    counter += step
            return outLst
        elif isinstance(index, int): # 不能直接 else
            currentNode = self.head
            while counter != index:
                currentNode = currentNode.next
                counter += 1
            if currentNode is not None:
                return currentNode.getData()
            else:
                raise StopIteration # 要判断是否超出边界，终止迭代
    
    def __str__(self):
        outLst = []
        currentNode = self.head
        while currentNode:
            outLst.append(repr(currentNode.getData()))
            currentNode = currentNode.next
        return '[ ' + ' |<->| '.join(outLst) + ' ]'
    
    def __iter__(self): # 捕捉for 循环时，调用一次
        self.currentNode = self.head
        return self
    
    def __next__(self): # for循环捕捉 stopiter 异常之前，都是调用这个 next
        if self.currentNode:
            data = self.currentNode.getData()
            self.currentNode = self.currentNode.next
            return data
        else:
            raise StopIteration

    def __eq__(self, other):
        if isinstance(other, type(self)):
            for i, j in zip(self, other): # 用 zip 把两个链表中的对象依次取出来配对，同时也利用了上面写的迭代器特性。
                if i != j:
                    return False
            return self.size() == other.size()
        else:
            return False