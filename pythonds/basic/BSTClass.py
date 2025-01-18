class BSTNode:
    def __init__(self, key, value, left=None, right=None, parent=None):
        self.key = key
        self.payload = value
        self.leftChild = left
        self.rightChild = right
        self.parent = parent

    def getLeftChild(self):
        return self.leftChild
    
    def getRightChild(self):
        return self.rightChild
    
    def getParent(self):
        return self.parent
    
    def isLeftChild(self):
        return self.parent and self.parent.getLeftChild == self
    
    def isRightChild(self):
        return self.parent and self.parent.getRightChild == self
    
    def isRoot(self):
        return not self.parent
    
    def isLeaf(self):
        return not self.leftChild and not self.rightChild
    
    def hasAnyChildren(self):
        return self.leftChild or self.rightChild
    
    def hasBothChildren(self):
        return self.leftChild and self.rightChild
    
    def replaceNodeData(self, key, value, leftC, rightC):
        self.key = key
        self.payload = value
        self.leftChild = leftC
        self.rightChild = rightC
        if self.getLeftChild():
            self.leftChild.parent = self
        if self.getRightChild():
            self.rightChild.parent = self
    
    def __iter__(self):
        if self.getLeftChild():
            for node in self.getLeftChild(): # can also write: yeild from self.getLeftChild() in replacement for for..in..yield..
                yield node
        yield self.key, self.payload
        if self.getRightChild():
            yield from self.getRightChild() # just like this. Both is the same.

class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0
    
    def lenth(self):
        return self.size
    
    def __len__(self):
        return self.size
    
    def __iter__(self):
        return self.root.__iter__()
    
    def put(self, key, value):
        if not self.root:
            self.root = BSTNode(key, value)
        else:
            self._put(key, value, self.root)
    
    def _put(self, key, value, currentNode):
        if key == currentNode.key:
            currentNode.payload = value # if the 2 keys match, overwrite the old payload with the new given value
        else:
            if key < currentNode.key: # given key is smaller than current node's key.
                if currentNode.getLeftChild():
                    self._put(key, value, currentNode.getLeftChild()) # recursion if there's already a left child
                else:
                    currentNode.leftChild = BSTNode(key, value, parent=currentNode) # found fit slot
                    self.size += 1
            else:
                if currentNode.getRightChild():
                    self._put(key, value, currentNode.getRightChild())
                else:
                    currentNode.rightChild = BSTNode(key, value, parent=currentNode)
                    self.size += 1
    
    def __setitem__(self, key, value):
        return self.put(key, value)

    # def get(self, key):
    #     if not self.root: # empty tree
    #         return None
    #     else:
    #         return self._get(key, self.root)
    
    def get(self, key, currentNode=False): # use False instead of None as None is what to expect when not found.
        if currentNode == False:
            currentNode = self.root
        if not currentNode:
            return None
        elif key == currentNode.key:
            return currentNode.payload
        elif key < currentNode.key:
            return self.get(key, currentNode.getLeftChild())
        else:
            return self.get(key, currentNode.getRightChild())

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return self.get(key) is not None

    def delete(self):
        pass


if __name__ == '__main__':
    testtree = BinarySearchTree()
    testtree.put(5,'five')
    testtree[6] = 'six'
    testtree[8] = 'eight'
    testtree[1] = '1one'
    print(testtree[3])
    testtree[3] = 'NEWthree'
    for k, v in testtree:
        print(f'key = {k}, value = {v}')
    
    from random import randint
    ttree = BinarySearchTree()
    for i in range(50):
        ttree.put(randint(1,100), '4tst')
    for k,v in ttree:
        print(f'key = {k}, value = {v}')
    print(len(ttree))
    print(ttree.root.key)