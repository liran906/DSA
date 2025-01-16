# http://python.openjudge.cn/2022dsa10/1/

# 思路
# 根据输入构建二叉树结构
# 中序遍历二叉树，把节点依次放入一个 stack（queue 也行啦）
# 输入的数字按从大到小排序
# 排序的数字依次赋值给stack中 pop 出来的节点的 value 上。
# 按层次遍历输出value

class BinaryTree:
    def __init__(self, key, value=None):
        self.value = value
        self.key = key # 为了应对这个题目，增加了一个 key 属性
        self.left = None
        self.right = None
    
    def insertLeft(self, key, newVal=None):
        newTree = BinaryTree(key, newVal)
        if self.left:
            newTree.left = self.left
        self.left = newTree
    
    def insertRight(self, key, newVal=None):
        newTree = BinaryTree(key, newVal)
        if self.right:
            newTree.right = self.right
        self.right = newTree
    
    def get(self, key):
        if self.key is None:
            raise KeyError('key not found')
        else:
            return self._get(self, key)
    
    def _get(self, tree, key):
        if not tree:
            return None
        if tree.key == key:
            return tree
        else:
            resultL = None
            resultR = None
            if tree.left:
                resultL = tree._get(tree.left, key)
                if resultL:
                    return resultL
            if tree.right:
                resultR = tree._get(tree.right, key)
            return resultR
    
    def travel(self): # 层次遍历
        queue = [self]
        travelLst = []
        while len(queue) > 0:
            currentTree = queue.pop(0)
            travelLst.append(currentTree.value)
            if currentTree.left:
                queue.append(currentTree.left)
            if currentTree.right:
                queue.append(currentTree.right)
        return travelLst
    
    def __iter__(self):
        if self.left:
            yield from self.left
        yield self
        if self.right:
            yield from self.right


def insertTree(couple, currentTree):
    if couple[0] != -1:
        currentTree.insertLeft(couple[0])
    if couple[1] != -1:
        currentTree.insertRight(couple[1])

def buildBT(alist):
    bTree = BinaryTree(0)
    for i in range(len(alist)):
        insertTree(alist[i], bTree.get(i))
    return bTree


n = int(input())
inlst = []
for i in range(n):
    inlst.append(tuple(map(int, input().split())))
numlst = list(map(int, input().split()))

mytree = buildBT(inlst)
treelst = []
for i in mytree:
    treelst.append(i)

for i in sorted(numlst,reverse=True):
    currentTree = treelst.pop()
    currentTree.value = i

out = ' '.join(list(map(str, mytree.travel())))
print(out)