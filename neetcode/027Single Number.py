# Single Number
# https://neetcode.io/problems/single-number
# e

# 手写造轮子
def xor(i1, i2):
    if i1 == i2:
        if isinstance(i1, int):
            return 0
        elif isinstance(i1, str):
            return '0'
    if i1 == 0 or i1 == '0':
        return i2
    if i2 == 0 or i2 == '0':
        return i1
    
    i1_2, i2_2 = encodeInto(i1, 2), encodeInto(i2, 2)
    if len(i1_2) > len(i2_2):
        i2_2 = '0' * (len(i1_2) - len(i2_2)) + i2_2
    elif len(i1_2) < len(i2_2):
        i1_2 = '0' * (len(i2_2) - len(i1_2)) + i1_2
    
    res = ''
    for d1, d2 in zip(i1_2, i2_2):
        res += xor(d1, d2)
    return decode(res, 2)
        

def encodeInto(num, base):
    tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    stack = []
    num = int(num)
    while num >= base:
        rem = num % base
        num = num // base
        stack.append(tmp[rem])
    if num > 0:
        stack.append(tmp[num])
    res = ''
    while stack:
        res += stack.pop()
    return res

def decode(num, base):
    tmp = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    res = 0
    cur = len(num) - 1
    for digit in str(num):
        res += tmp.index(digit) * base ** cur
        cur -= 1
    return res

class Solution:
    def singleNumber(self, nums):
        res = 0
        for n in nums:
            res = xor(res, n)
        return res

# use Python's implemented XOR method
class Solution:
    def singleNumber(self, nums):
        res = 0
        for n in nums:
            res = res ^ n
        return res