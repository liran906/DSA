#uuid_share#  b8aadd51-40f7-46f6-9b73-514950f3c118  #
# PKUDSA 课程上机作业
# 【H4】AVL树作业
#
# 说明：为方便批改作业，请同学们在完成作业时注意并遵守下面规则：
# （1）直接在本文件中指定部位编写代码
# （2）如果作业中对相关类有明确命名/参数/返回值要求的，请严格按照要求执行
# （3）有些习题会对代码的编写进行特殊限制，请注意这些限制并遵守
# （4）作业代码部分在DDL之前提交到教学网

# ---- 用AVL树实现字典类型 ----
# 用AVL树来实现字典类型，使得其put/get/in/del操作均达到对数性能
# 采用如下的类定义，至少实现下列的方法
# key至少支持整数、浮点数、字符串
# 请调用hash(key)来作为AVL树的节点key
# 【注意】涉及到输出的__str__, keys, values这些方法的输出次序是AVL树中序遍历次序
#    也就是按照hash(key)来排序的，这个跟Python 3.7中的dict输出次序不一样。

# 请在此编写你的代码


class TreeNode:
    """
    二叉树节点
    请自行完成节点内部的实现，并实现给出的接口
    """
    def __init__(self, key, val=None, par=None, lc=None, rc=None):  # 初始化方法
        self.key = key
        self.value = val
        self.parent = par
        self.leftChild = lc
        self.rightChild = rc
        self.height = 1
        self.balance = 0
    
    # def update(self):
    #     lh = self.leftChild.height if self.getLeft() else 0
    #     rh = self.rightChild.height if self.getRight() else 0
    #     newHeight = max(lh, rh) + 1
    #     self.balance = lh - rh

    #     if self.height != newHeight:
    #         self.height = newHeight
    #         if self.parent:
    #             self.parent.update()
    
    # def getHeight(self):
    #     lh = self.leftChild.height if self.getLeft() else 0
    #     rh = self.rightChild.height if self.getRight() else 0
    #     return max(lh, rh) + 1
    
    # def updateHeight(self):
    #     originalHeight = self.height
    #     self.height = self.getHeight()
    #     if self.parent and self.height != originalHeight:
    #         self.parent.updateHeight()
    
    # def getBalance(self):
    #     lh = self.leftChild.height if self.getLeft() else 0
    #     rh = self.rightChild.height if self.getRight() else 0
    #     return lh - rh
    
    # def updateBalance(self):
    #     originalBalance = self.balance
    #     self.balance = self.getBalance()
    #     if self.balance != 0 and self.balance != originalBalance:
    #         if self.balance > 1 or self.balance < -1:
    #             self.rebalance()
    #         if self.parent:
    #             self.parent.updateBalance()
    
    # def rebalance(self):
    #     if self.balance > 1:
    #         if self.leftChild.balance < 0:
    #             self.leftChild.rotateLeft()
    #             self.rotateRight()
    #         else:
    #             self.rotateRight()
    #     elif self.balance < -1:
    #         if self.rightChild.balance > 0:
    #             self.rightChild.rotateRight()
    #             self.rotateLeft()
    #         else:
    #             self.rotateLeft()
        
    #     self.update()
    
    # def rotateRight(self):
    #     newParent = self.leftChild
    #     currentParent = self.parent
    #     if currentParent:
    #         if self.isLeftChild():
    #             currentParent.leftChild = newParent
    #         else:
    #             currentParent.rightChild = newParent
        
    #     self.parent = newParent
    #     newParent.parent = currentParent
    #     if newParent.rightChild:
    #         self.leftChild = newParent.rightChild
    #         newParent.rightChild.parent = self
    #     else:
    #         self.leftChild = None
    #     newParent.rightChild = self
    
    # def rotateLeft(self):
    #     newParent = self.rightChild
    #     currentParent = self.parent
    #     if currentParent:
    #         if self.isLeftChild():
    #             currentParent.leftChild = newParent
    #         else:
    #             currentParent.rightChild = newParent

    #     self.parent = newParent
    #     newParent.parent = currentParent
    #     if newParent.leftChild:
    #         self.rightChild = newParent.leftChild
    #         newParent.leftChild.parent = self
    #     else:
    #         self.rightChild = None
    #     newParent.leftChild = self

    def getParent(self):
        return self.parent

    def getLeft(self):  # 获取左子树 (不存在时返回None)
        return self.leftChild

    def getRight(self):  # 获取右子树 (不存在时返回None)
        return self.rightChild
    
    def setParent(self, par):
        if isinstance(par, TreeNode) or par is None:
            self.parent = par

    def setLeft(self, left):
        if isinstance(left, TreeNode) or left is None:
            self.leftChild = left
    
    def setRight(self, right):
        if isinstance(right, TreeNode) or right is None:
            self.rightChild = right
    
    def isRoot(self):
        return self.parent == None
    
    def isLeaf(self):
        return not self.leftChild and not self.rightChild
    
    def isLeftChild(self):
        if self.parent:
            return self == self.parent.leftChild
        return False
    
    def isRightChild(self):
        if self.parent:
            return self == self.parent.rightChild
        return False

    def hasBothChildren(self):
        return self.leftChild and self.rightChild

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
                if self.getLeft():
                    self.leftChild.parent = self.parent
                    self.parent.leftChild = self.leftChild
                else: # has right child
                    self.rightChild.parent = self.parent
                    self.parent.leftChild = self.rightChild
            else: # is right child
                if self.getLeft():
                    self.leftChild.parent = self.parent
                    self.parent.rightChild = self.leftChild
                else: # has right child
                    self.rightChild.parent = self.parent
                    self.parent.rightChild = self.rightChild

class mydict:
    """
    以AVL树作为内部实现的字典
    """
    def getRoot(self):  # 返回内部的AVL树根
        return self.root

    def __init__(self):  # 创建一个空字典
        self.root = None
        self.size = 0
    
    def put(self, key, value=None):
        if not self.root:
            self.root = TreeNode(key, value)
        else:
            self._put(self.root, key, value)
        self.size += 1

    def _put(self, parentNode, key, value):
        if key < parentNode.key:
            if parentNode.getLeft():
                self._put(parentNode.getLeft(), key, value)
            else:
                parentNode.leftChild = TreeNode(key, value, parentNode)
                self.updateBalance(parentNode)

        elif key > parentNode.key:
            if parentNode.getRight():
                self._put(parentNode.getRight(), key, value)
            else:
                parentNode.rightChild = TreeNode(key, value, parentNode)
                self.updateBalance(parentNode)

        else: # key = parentNode.key
            parentNode.value = value
            self.size -= 1
    
    def updateBalance(self, node):
        lh = node.leftChild.height if node.getLeft() else 0
        rh = node.rightChild.height if node.getRight() else 0
        newHeight = max(lh, rh) + 1
        node.balance = lh - rh

        if abs(node.balance) > 1:
            self.rebalance(node)
            return

        if node.height != newHeight:
            node.height = newHeight
            if node.parent:
                self.updateBalance(node.parent)
    
    def rebalance(self, node):
        if node.balance > 1:
            if node.leftChild.balance < 0:
                # Do an RL Rotation
                self.rotateLeft(node.leftChild)
                self.rotateRight(node)
            else:
                # single right
                self.rotateRight(node)
        elif node.balance < -1:
            if node.rightChild.balance > 0:
                # Do an LR Rotation
                self.rotateRight(node.rightChild)
                self.rotateLeft(node)
            else:
                # single left
                self.rotateLeft(node)
        
        # self.update()
    
    def rotateRight(self, node):
        newParent = node.leftChild
        if node.isRoot():
            self.root = newParent
            newParent.parent = None
        else:
            currentParent = node.parent
            if node.isLeftChild():
                currentParent.leftChild = newParent
            else:
                currentParent.rightChild = newParent
            newParent.parent = currentParent
        
        node.leftChild = newParent.rightChild
        if newParent.rightChild:
            newParent.rightChild.parent = node
        newParent.rightChild = node
        node.parent = newParent
        self.updateBalance(node)
    
    def rotateLeft(self, node):
        newParent = node.rightChild
        if node.isRoot():
            self.root = newParent
            newParent.parent = None
        else:
            currentParent = node.parent
            if node.isLeftChild():
                currentParent.leftChild = newParent
            else:
                currentParent.rightChild = newParent
            newParent.parent = currentParent
        
        node.rightChild = newParent.leftChild
        if newParent.leftChild:
            newParent.leftChild.parent = node
        newParent.leftChild = node
        node.parent = newParent
        self.updateBalance(node)
    
    def get(self, key):
        if self.root is None:
            raise KeyError('key does not exist')
        else:
            node = self._get(self.root, key)
            return node.value
    
    def _get(self, node, key):
        if key == node.key:
            return node
        elif key < node.key:
            if node.leftChild:
                return self._get(node.leftChild, key)
            else:
                raise KeyError('key does not exist')
        else:
            if node.rightChild:
                return self._get(node.rightChild, key)
            else:
                raise KeyError('key does not exist')


    def __setitem__(self, key, value):  # 将key:value保存到字典
        return self.put(key, value)

    def __getitem__(self, key):  # 从字典中根据key获取value
        # v = md[key]
        # key在字典中不存在的话，请raise KeyError
        return self.get(key)

    def delete(self, key):
        # use get method first, then remove
        if self.size > 1:
            nodeToDelete = self._get(self.root, key)
            if nodeToDelete:
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
        # del md[key]
        # key在字典中不存在的话，请raise KeyError
        return self.delete(key)
    
    def remove(self, currentNode):
        if currentNode.isLeaf(): # no children
            if currentNode.isLeftChild():
                currentNode.parent.leftChild = None
            else:
                currentNode.parent.rightChild = None
            self.updateBalance(currentNode.parent)
        
        elif currentNode.hasBothChildren(): # two children
            successor = currentNode.rightChild.findSuccessor()
            # okay to write as below, only deletes the links linking to it.
            # PROBLEM IS FINDING THE KEY IN GET METHOD OVER AGAIN: RECALCULATION.
            # self.delete(successor.key)
            successor.spliceOut()
            currentNode.key = successor.key
            currentNode.value = successor.value

        else: # only one child
            leftChild = currentNode.getLeft()
            rightChild = currentNode.getRight()
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

    def __len__(self):  # 获取字典的长度
        # l = len(md)
        return self.size

    def __contains__(self, key):  # 判断字典中是否存在key
        # k in md
        try:
            result = self._get(self.root, key)
        except KeyError:
            return False
        return result is not None

    def clear(self):  # 清除字典
        self.root = None
        self.size = 0

    def __str__(self):  # 输出字符串形式，参照内置dict类型，输出按照AVL树中序遍历次序
        # 格式类似：{'name': 'sessdsa', 'hello': 'world'}
        if self.root is None:
            return '{}'
        results = self.inorder()
        return '{' + ', '.join([f'{k}: {v}' for k, v in results]) + '}'

    __repr__ = __str__

    def keys(self):  # 返回所有的key，类型是列表，按照AVL树中序遍历次序
        return self.inorder(val=False)

    def values(self):  # 返回所有的value，类型是列表，按照AVL树中序遍历次序
        return self.inorder(key=False)

    def inorder(self, key=True, val=True):
        results = []
        self._inorder(self.root, key, val, results)
        return results
    
    def _inorder(self, node, key, val, results):
        if node is None:
            return
        if key and val:
            results.append((node.key, node.value))
        elif key:
            results.append(node.key)
        elif val:
            results.append(node.value)
        self._inorder(node.leftChild, key, val, results)
        self._inorder(node.rightChild, key, val, results)

# 代码结束

#mydict=dict
# 检验
print("========= AVL树实现字典 =========")
md = mydict()
# md['hello'] = 'world'
# md['name'] = 'sessdsa'
print(md)  # {'name': 'sessdsa', 'hello': 'world'}

for f in range(1000):
    md[f**0.5] = f

for i in range(1000, 2000):
    md[i] = i**2

print(len(md))  # 2002
print(md[2.0])  # 4
print(md[1000])  # 1000000
# print(md['hello'])  # world
print(20.0 in md)  # True
print(99 in md)  # False

# del md['hello']
# print('hello' in md)  # False
for i in range(1000, 2000):
    del md[i]
print(len(md))  # 1001
for f in range(1000):
    del md[f**0.5]
    if f + len(md) != 999:
        print('fffff'+str(f))
        break
print(len(md))  # 1
print(md.keys())  # ['name']
print(md.values())  # ['sessdsa']
for a in md.keys():
    print(md[a])  # sessdsa
md.clear()
print(md)  # {}