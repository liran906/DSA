import sys
sys.path.append('.')
from pythonds.basic.stack import Stack
from pythonds.basic.BinaryTree import BinaryTree

def buildParseTree(expresion):
    expresionLst = list(expresion.split()) # 输入每个对象之间要加空格
    parentStack = Stack()
    expresionTree = BinaryTree()
    currentTree = expresionTree
    parentStack.push(currentTree) # 这一行必须要，不然最后一个右括号 pop 不出来了

    for i in expresionLst:
        if i == '(':
            currentTree.insertLeft()
            parentStack.push(currentTree)
            currentTree = currentTree.getLeftChild()
        elif i not in '+-*/)': # 不能用in数字（多位数会出错）
            currentTree.setRootVal(int(i))
            currentTree = parentStack.pop()
        elif i in '+-*/':
            currentTree.setRootVal(i)
            currentTree.insertRight()
            parentStack.push(currentTree)
            currentTree = currentTree.getRightChild()
        elif i == ')':
            currentTree = parentStack.pop()
        else:
            raise ValueError
    return expresionTree

def doMath(op, num1, num2):
    if op == '+':
        return num1 + num2
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 * num2
    elif op == '/':
        return num1 / num2

# 这个考虑的不够透彻
# def evaluate(tree):
#     if tree.getLeftChild() is None and tree.getRightChild() is None:
#         return tree.getRootVal()
#     else:
#         if tree.getLeftChild() in '+-*/':
#             leftResult = evaluate(tree.getLeftChild())
#         elif tree.getRightChild() in '+-*/':
#             rightResult = evaluate(tree.getRightChild())
#         elif tree.getLeftChild() not in '+-*/':
#             leftTree = tree.getLeftChild()
#             num1 = leftTree.getRootVal()
#             leftTree.setRootVal(None)

#             rightTree = tree.getRightChild()
#             num2 = rightTree.getRootVal()
#             rightTree.setRootVal(None)

#             operand = tree.getRootVal()
#             tree.setRootVal(doMath(operand, num1, num2))

def evaluate(tree):
    # tree = BinaryTree() # 可以临时打开这行，看的清楚一点
    if tree.getLeftChild() is None and tree.getRightChild() is None:
        return tree.getRootVal()
    else:
        leftResult = evaluate(tree.getLeftChild())
        rightResult = evaluate(tree.getRightChild())
        operand = tree.getRootVal()
        return doMath(operand, leftResult, rightResult)

# 陈斌方法，更简洁。不需要 domath 方法
import operator
def evaluate(tree):
    operand = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    leftChild, rightChild = tree.getLeftChild(), tree.getRightChild()

    if not leftChild and not rightChild:
        return tree.getRootVal()
    else:
        fn = operand[tree.getRootVal()]
        return fn(evaluate(leftChild), evaluate(rightChild))

def tree2expression(tree):
    left, right = tree.getLeftChild(), tree.getRightChild()
    if left and right:
        return '(' + str(tree2expression(left)) + tree.getRootVal() + str(tree2expression(right)) + ')'
    else:
        return str(tree.getRootVal())


if __name__ == '__main__':
    exp = '( ( 3 * 5 ) * ( 4 + ( 10 - 12 ) ) )'
    print(evaluate(buildParseTree(exp)))
    print(tree2expression(buildParseTree(exp)))