# 1:二叉树复原
# 总时间限制: 1000ms 内存限制: 65536kB
# 描述
# 给定一种序列化二叉树的方式：从根节点起始按层次遍历二叉树所有“可能”存在节点的位置：若该位置存在节点，则输出节点值，并在下一层相应增加两个可用位置；否则输出None，且不增加下一层的可用位置。
# 例如"[5, 4, 7, 3, None, 2, None, -1, None, 9]"是下面所示的二叉树序列化的结果，其中结构为【本节点，【左子树】，【右子树】】：
# 【5，【4，【3，【-1，【】，【】】，【】】，【】】，【7，【2，【9，【】，【】】，【】】，【】】】

# 现给出一个二叉树以这种形式序列化的结果，请复原该二叉树并给出它的中序遍历。
# 输入格式:
# 一行合法的Python表达式，可解析为包含整数与None的列表
# 输出格式：
# 二叉树中序遍历的整数序列，以空格分隔

# 输入样例：
# [5, 4, 7, 3, None, 2, None, -1, None, 9]
# 输出样例：
# -1 3 4 5 9 2 7

# 输入样例2：
# [5,1,4,None,None,3,6]
# 输出样例2：
# 1 5 3 4 6

# 输入
# 一行合法的Python表达式，可解析为包含整数与None的列表
# 输出
# 二叉树中序遍历的整数序列，以空格分隔

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

def fixBT(alist):
    tree = BinaryTree(alist[0])
    index = 1
    queue = [tree]

    while len(queue) > 0 and index < len(alist):
        current = queue.pop(0)

        if current.getRootVal() is not None and index < len(alist):
            current.insertLeft(alist[index])
            left = current.getLeftChild()
            queue.append(left)
            index += 1
        
        if current.getRootVal() is not None and index < len(alist):
            current.insertRight(alist[index])
            right = current.getRightChild()
            queue.append(right)
            index += 1
    
    return tree

def printtree(tree):
    result = []
    def inOrder(tree):
        left = tree.getLeftChild()
        right = tree.getRightChild()
        if left and left.getRootVal():
            inOrder(left)
        result.append(str(tree.getRootVal()))
        if right and right.getRootVal():
            inOrder(right)
    
    inOrder(tree)
    return ' '.join(result)


inlst = eval(input())
tree = fixBT(inlst)
print(printtree(tree))