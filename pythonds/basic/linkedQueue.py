class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None
        self.prev = None
    
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
    
    def setData(self, newdata):
        self.data = newdata
    
    def setNext(self, newnext):
        self.next = newnext
    
    def setPrev(self, newprev):
        self.prev = newprev

class LinkedQueue:
    def __init__(self):
        self.head = None
        self.tail = None
        self.lenth = 0
    
    def enqueue(self, item):
        newNode = Node(item)
        if self.lenth == 0:
            self.head = newNode
            self.tail = newNode
        else:
            currentNode = self.tail
            self.tail = newNode
            newNode.setPrev(currentNode)
            currentNode.setNext(newNode)
        self.lenth += 1
    
    def dequeue(self):
        if not self.head:
            return None
        currentNode = self.head
        nextNode = currentNode.getNext()
        self.head = nextNode
        if nextNode:
            nextNode.setPrev(None)
        self.lenth -= 1
        return currentNode.getData()
    
    def size(self):
        return self.lenth
    
    def isEmpty(self):
        return self.lenth == 0

if __name__ == '__main__':
    q = LinkedQueue()
    for i in [_ for _ in range(20)]:
        q.enqueue(i)
    print(q.dequeue())
    print(q.dequeue())
    print(q.dequeue())
    print(q.size())