import sys
sys.path.append('.')
from pythonds.basic.node import Node

class Orderedlist:
    def __init__(self):
        self.head = None
    
    def add(self, item):
        newNode = Node(item)
        currentNode = self.head
        prevNode = None

        while currentNode != None: # 循环直到当前 node 比 newnode 大
            if currentNode.getData() > newNode.getData():
                break
            prevNode = currentNode
            currentNode = currentNode.getNext()
        
        if prevNode == None:
            newNode.setNext(self.head)
            self.head = newNode
        else:
            newNode.setNext(currentNode)
            prevNode.setNext(newNode)
    
    def remove(self, item):
        currentNode = self.head
        prevNode = None

        while currentNode != None:
            if currentNode.getData() == item:
                if prevNode == None: # 删除的是第一个
                    self.head = self.head.getNext()
                else:
                    prevNode.setNext(currentNode.getNext())
                return True
            elif currentNode.getData() > item:
                break
            else:
                prevNode = currentNode
                currentNode = currentNode.getNext()
        return False
    
    def search(self, item):
        currentNode = self.head

        while currentNode != None:
            if currentNode.getData() == item:
                return True
            elif currentNode.getData() > item:
                return False
            else:
                currentNode = currentNode.getNext()
        return False
    
    def isEmpty(self):
        return self.head == None
    
    def size(self):
        currentNode = self.head
        counter = 0

        while currentNode != None:
            currentNode = currentNode.getNext()
            counter += 1
        return counter
    
    def pop(self, pos = None):
        currentNode = self.head
        prevNode = None
        counter = 0

        while currentNode.getNext() != None and counter != pos:
            prevNode = currentNode
            currentNode = currentNode.getNext()
            counter += 1
        if pos == 0: # 删第一个
            self.head = self.head.getNext()
        else:
            prevNode.setNext(currentNode.getNext())
        return currentNode.getData()