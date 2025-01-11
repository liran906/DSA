import sys
sys.path.append('.')

from pythonds.basic.stack import Stack

# 运用栈，检测一个字符串中所有圆括号是否符合逻辑
def is_par(item):
    par_stack = Stack()
    if isinstance(item, str):
        for i in range(len(item)):
            if item[i] in ['(', ')']:
                if item[i] == '(':
                    par_stack.push('1')
                elif item[i] == ')':
                    if par_stack.isEmpty():
                        return False
                    par_stack.pop()
        if par_stack.isEmpty():
            return True
        return False
    return False

print(is_par('((1+2)?(3-4))=(wo)'))

# 运用栈，检测一个字符串中所有括号是否符合逻辑
def check_bracket(item):
    if not isinstance(item, str):
        return False
    check = Stack()

    for i in range(len(item)):
        if item[i] in ['(', ')', '[', ']', '{', '}']:
            if item[i] == '(':
                check.push('r')
            elif item[i] == '[':
                check.push('s')
            elif item[i] == '{':
                check.push('c')
            elif item[i] == ')':
                if check.peek() == 'r':
                    check.pop()
                else:
                    return False
            elif item[i] == ']':
                if check.peek() == 's':
                    check.pop()
                else:
                    return False
            elif item[i] == '}':
                if check.peek() == 'c':
                    check.pop()
                else:
                    return False
    if check.isEmpty:
        return True
    return False

print(check_bracket('([{(d),[[],{d,}]},])'))

# 简化一下代码
def check_bracket2(item):
    if not isinstance(item, str):
        return False
    check = Stack()
    for i in range(len(item)):
        if item[i] in '([{':
            check.push(item[i])
        elif item[i] in ')]}':
            if check.peek() == reverse(item[i]):
                check.pop()
            else:
                return False
    if check.isEmpty():
        return True
    return False

def reverse(inp):
    left = '([{'
    right = ')]}'
    if inp in left:
        return right[left.index(inp)]
    return left[right.index(inp)]

if __name__ == '__main__':
    print(check_bracket2('([{(d),[[],{d,}]},])'))