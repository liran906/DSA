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
        return self.parent and self.parent.getLeftChild() == self
    
    def isRightChild(self):
        return self.parent and self.parent.getRightChild() == self
    
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
    
    def findSuccessor(self): # find the smallest key in right child.
        if not self.leftChild:
            return self
        else:
            return self.leftChild.findSuccessor()

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.leftChild = None
            else:
                self.parent.rightChild = None
        elif self.hasBothChildren():
            pass # isnt used in BST algrothrim. Leaving blank for future codings.
        else: # has one child
            if self.isLeftChild():
                if self.getLeftChild():
                    self.leftChild.parent = self.parent
                    self.parent.leftChild = self.leftChild
                else: # has right child
                    self.rightChild.parent = self.parent
                    self.parent.leftChild = self.rightChild
            else: # is right child
                if self.getLeftChild():
                    self.leftChild.parent = self.parent
                    self.parent.rightChild = self.leftChild
                else: # has right child
                    self.rightChild.parent = self.parent
                    self.parent.rightChild = self.rightChild

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
    
    def put(self, key, value=None):
        if not self.root:
            self.root = BSTNode(key, value)
        else:
            self._put(key, value, self.root)
        self.size += 1
    
    def _put(self, key, value, currentNode):
        if key == currentNode.key:
            currentNode.payload = value # if the 2 keys match, overwrite the old payload with the new given value
            self.size -= 1 # 抵消外面的+1
        else:
            if key < currentNode.key: # given key is smaller than current node's key.
                if currentNode.getLeftChild():
                    self._put(key, value, currentNode.getLeftChild()) # recursion if there's already a left child
                else:
                    currentNode.leftChild = BSTNode(key, value, parent=currentNode) # found fit slot
            else:
                if currentNode.getRightChild():
                    self._put(key, value, currentNode.getRightChild())
                else:
                    currentNode.rightChild = BSTNode(key, value, parent=currentNode)
    
    def __setitem__(self, key, value):
        return self.put(key, value)

    def get(self, key): # returns the key and value
        if not self.root: # empty tree
            return None
        else:
            return self._get(key, self.root)
    
    def _get(self, key, currentNode=False):  # returns the node
        # use False instead of None as None is what to expect when not found.
        if currentNode == False:
            currentNode = self.root
        if not currentNode:
            return None
        elif key == currentNode.key:
            return currentNode
        elif key < currentNode.key:
            return self._get(key, currentNode.getLeftChild())
        else:
            return self._get(key, currentNode.getRightChild())

    def __getitem__(self, key):
        return self.get(key)

    def __contains__(self, key):
        return self._get(key) is not None

    def delete(self, key):
        # use get method first, then remove
        if self.size > 1:
            nodeToDelete = self._get(key)
            if not nodeToDelete:
                raise KeyError('Key does not exist')
            self.remove(nodeToDelete)
            self.size -= 1
        
        # deleting tree with only node: root
        elif self.size == 1 and key == self.root.key:
            self.root = None
            self.size -= 1
        
        # empty tree. Include size==1 but key != root.key
        else:
            raise KeyError('Key does not exist')
    
    def __delitem__(self, key):
        return self.delete(key)
    
    def remove(self, currentNode):
        if currentNode.isLeaf(): # no children
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
        
        elif currentNode.hasBothChildren(): # two children
            successor = currentNode.rightChild.findSuccessor()
            # okay to write as below, only deletes the links linking to it.
            # PROBLEM IS FINDING THE KEY IN GET METHOD OVER AGAIN: RECALCULATION.
            # self.delete(successor.key)
            successor.spliceOut()
            currentNode.key = successor.key
            currentNode.payload = successor.payload

        else: # only one child
            leftChild = currentNode.getLeftChild()
            rightChild = currentNode.getRightChild()
            if currentNode.isLeftChild():
                if leftChild:
                    leftChild.parent = currentNode.parent
                    currentNode.parent.leftChild = leftChild
                else: # has right child
                    rightChild.parent = currentNode.parent
                    currentNode.parent.leftChild = rightChild
            
            elif currentNode.isRightChild():
                if leftChild:
                    leftChild.parent = currentNode.parent
                    currentNode.parent.rightChild = leftChild
                else: # has right child
                    rightChild.parent = currentNode.parent
                    currentNode.parent.rightChild = rightChild
            
            else: # is not a child, aka is root
                if leftChild:
                    leftChild.parent = None
                    self.root = leftChild
                else:
                    rightChild.parent = None
                    self.root = rightChild

if __name__ == '__main__':
    from random import randint
    ttree = BinarySearchTree()
    for i in range(100):
        ttree.put(randint(1,10000))
    for i in ttree:
        print(i, end=', ')
    print(len(ttree))