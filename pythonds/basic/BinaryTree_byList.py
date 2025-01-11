def binaryTree(root):
    return [root, [], []]

def insertLeft(root, newBranch):
    t = root.pop(1)
    if len(t) > 1:
        root.insert(1, [newBranch, t, []])
    else:
        root.insert(1, [newBranch, [], []])

def insertRight(root, newBranch):
    t = root.pop(2)
    if len(t) > 1:
        root.insert(2, [newBranch, [], t])
    else:
        root.insert(2, [newBranch, [], []])

def getRootVal(root):
    return root[0]

def setRootVal(root, value):
    root[0] = value

def getLeftChild(root):
    return root[1]

def getRightChild(root):
    return root[2]

if __name__ == '__main__':
    t = binaryTree(3)
    insertLeft(t, 4)
    insertLeft(t, 5)
    insertRight(t, 6)
    insertRight(t, 7)
    lc = getLeftChild(t)
    llc = getLeftChild(getLeftChild(t))
    print(lc)
    print(llc)

    setRootVal(lc, 9)
    print(t)
    insertLeft(lc, 11)
    print(t)
    print(getRightChild(getRightChild(t)))