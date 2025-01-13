# 3:多叉树遍历

# 总时间限制: 1000ms 内存限制: 65536kB
# 描述
# 给定以嵌套列表形式给出的多叉树，求它的后序遍历
# 注：每个代表非空多叉树的列表包含至少一项；列表第一项代表节点值，其后每一项分别为子树；遍历子树时以列表下标从小到大的顺序进行。

# 输入
# 一行合法的Python表达式，可解析为嵌套列表形式的多叉树结构
# 输出
# 一行整数，以空格分隔
# 样例输入
# [1,[2,[3,[4],[5]],[6]],[7],[8,[9],[10]]]
# 样例输出
# 4 5 3 6 2 7 9 10 8 1

class MultiTree:
    def __init__(self, value=None):
        self.value = value
        self.children = []
        self.numOfChildren = len(self.children)
        self.outputLst = []
    
    def addChild(self, value=None):
        self.numOfChildren += 1
        self.children.append(MultiTree(value))
    
    def getRootVal(self):
        return self.value
    
    def setRootVal(self, newVal):
        self.value = newVal
    
    def getChild(self, index=0):
        return self.children[index]
    
    def postOrder(self):
        if self.numOfChildren == 0:
            self.outputLst.append(self.value)
        else:
            for i in self.children:
                clist = i.postOrder()
                self.outputLst.extend(clist)
            self.outputLst.append(self.value)
        return self.outputLst

def fixTree(tree, alist):
    if not tree.getRootVal():
        tree.setRootVal(alist[0])
    for i in range(1, len(alist)):
        tree.addChild(alist[i][0])
        if len(alist[i]) > 1:
            fixTree(tree.getChild(i-1), alist[i])

def post_order(alist):
    if len(alist) == 1:
        return alist
    else:
        mylist = []
        for i in range(1, len(alist)):
            mylist.extend(post_order(alist[i]))
        mylist.append(alist[0])
        return mylist


mytree = MultiTree()
# lst = [1,[2,[3,[4],[5]],[6]],[7],[8,[9],[10]]]
lst = eval(input())

fixTree(mytree, lst)
print(' '.join (list(map(str, mytree.postOrder()))))

# 方案二：
def post_order(alist):
    if len(alist) == 1:
        return alist
    else:
        mylist = []
        for i in range(1, len(alist)):
            mylist.extend(post_order(alist[i]))
        mylist.append(alist[0])
        return mylist

lst = eval(input())
print(' '.join (list(map(str, post_order(lst)))))