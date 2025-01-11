# 不需要 Node 类。链表实现看 BinaryTree.py
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def setVal(self, newVal):
        self.value = newVal

    def getVal(self):
        return self.value

    def setLeft(self, newNode):
        self.left = newNode
    
    def setRight(self, newNode):
        self.right = newNode
    
    def getLeft(self):
        return self.left
    
    def getRight(self):
        return self.right

class BinaryTree:
    def __init__(self, value):
        self.root = Node(value)
    
    def insertLeft(self, newVal):
        newNode = Node(newVal)
        curLeft = self.root.getLeft()
        if curLeft:
            newNode.setLeft(curLeft)
        self.root.setLeft(newNode)
    
    def insertRight(self, newVal):
        newNode = Node(newVal)
        curRight = self.root.getRight()
        if curRight:
            newNode.setRight(curRight)
        self.root.setRight(newNode)
    
    def getRootVal(self):
        return self.root.getVal()
    
    def setRootVal(self, newVal):
        self.root.setVal(newVal)
    
    def getLeftChild(self):
        return self.root.getLeft()
    
    def getRightChild(self):
        return self.root.getRight()


if __name__ == '__main__':
    t = BinaryTree(3)
    t.insertLeft(4)
    t.insertLeft(5)
    t.insertRight(6)
    t.insertRight(7)
    lc = t.getLeftChild().getLeft()
    print(lc.getVal())