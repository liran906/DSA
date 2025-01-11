class BinaryTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None
    
    def insertLeft(self, newVal=None):
        newTree = BinaryTree(newVal)
        if self.left:
            newTree.left = self.left
        self.left = newTree
    
    def insertRight(self, newVal=None):
        newTree = BinaryTree(newVal)
        if self.right:
            newTree.right = self.right
        self.right = newTree
    
    def getRootVal(self):
        return self.value
    
    def setRootVal(self, newVal):
        self.value = newVal
    
    def getLeftChild(self):
        return self.left
    
    def getRightChild(self):
        return self.right
    
    def preorder(self):
        print(self.getRootVal())
        if self.left:
            self.getLeftChild().preorder()
        if self.right:
            self.getRightChild().preorder()
    
    def inorder(self):
        if self.left:
            self.getLeftChild().inorder()
        print(self.getRootVal())
        if self.right:
            self.getRightChild().inorder()
    
    def postorder(self):
        if self.left:
            self.getLeftChild().postorder()
        if self.right:
            self.getRightChild().postorder()
        print(self.getRootVal())

    def __repr__(self):
        left = repr(self.left) if self.left else ''
        right = repr(self.right) if self.right else ''
        return f'{self.value} -< {left} | {right} >'


if __name__ == '__main__':
    t = BinaryTree(3)
    t.insertLeft(4)
    t.insertLeft(5)
    t.insertRight(6)
    t.insertRight(7)
    print(t)
    lc = t.getLeftChild()
    llc = lc.getLeftChild()
    print(lc)
    print(llc)

    lc.setRootVal(9)
    print(t)
    lc.insertLeft(11)
    print(t)
    print(t.getRightChild().getRightChild())

    print('inorder')
    t.inorder()