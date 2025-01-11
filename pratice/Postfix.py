import sys
sys.path.append('.')
from pythonds.basic.stack import Stack

def infix2postfix(input):
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    para = Stack()
    cal = Stack()
    postfix_lst = []

    for i in str(input):
        if i == '(':
            para.push(i)
            cal.push(i)
        elif i == ')':
            if not para.isEmpty():
                para.pop()
                while cal.peek() != '(': # 输出运算符直到左括号
                    postfix_lst.append(cal.pop())
                cal.pop() # 删掉左括号
            else:
                return 'error'
        elif i.isalnum(): # i是数字或字母
            postfix_lst.append(i)
        elif i in prec.keys():
            if cal.isEmpty():
                cal.push(i)
            else:
                if prec[i] > prec[cal.peek()]:
                    cal.push(i)
                elif  prec[i] == prec[cal.peek()]:
                    postfix_lst.append(cal.pop())
                    cal.push(i)
                elif prec[i] < prec[cal.peek()]:
                    while (not cal.isEmpty()) and (cal.peek() != '('):
                        postfix_lst.append(cal.pop())
                    cal.push(i)
    while not cal.isEmpty():
        postfix_lst.append(cal.pop())
    
    return (''.join(postfix_lst))

def infix2postfix2(input):
    # 写这段代码一个难点是操作数和操作符之间要均匀加上空格，因为要应对两位以上数字的情况，数字之间不能加空格
    # 一开始试过每到操作数时，增加一个空格，发现加上各种括号的逻辑之后总有多的括号或者缺少的括号
    # 最终先行判断读取数据是否是连续字符或者数字，如果是，则作为一个整体 buffer 进入 lst 中
    prec = {'*': 3, '/': 3, '+': 2, '-': 2, '(': 1}
    notation_stack = Stack()
    output_lst = []
    buffer = ''

    for i in str(input):
        if i.isalnum():
            buffer += i
        else:
            if buffer:
                output_lst.append(buffer)
                buffer = ''
            if i == '(':
                notation_stack.push(i)
            elif i == ')':
                while notation_stack.peek() != '(':
                    output_lst.append(notation_stack.pop())
                notation_stack.pop() # 删除对应左括号
            elif i in prec.keys():
                while (not notation_stack.isEmpty()) and (prec[i] <= prec[notation_stack.peek()]):
                    output_lst.append(notation_stack.pop())
                notation_stack.push(i)
    if buffer:
        output_lst.append(buffer) # 缓存中存余的数据要加上

    while not notation_stack.isEmpty():
        output_lst.append(notation_stack.pop())
    
    return ' '.join(output_lst)

import operator # 引入 operator 为了把对应字符转换为运算

def postfix_calculate(input):
    lst = input.split()
    stk = Stack()
    prec = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}
    for i in lst:
        if i in prec:
            cal_1 = stk.pop()
            cal_2 = stk.pop()
            result = prec[i](cal_2, cal_1) # 注意顺序！
            stk.push(result)
        else:
            stk.push(float(i))
        print('|', stk)
    return result

if __name__ == '__main__':

    eq = '4-9+6'
    eq_r = eval(eq)
    print(eq,'=')
    print(infix2postfix2(eq))
    result0 = postfix_calculate(infix2postfix2(eq))
    print(f'{result0} Answer is {result0 == eq_r}')