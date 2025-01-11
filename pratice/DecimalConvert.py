# 十进制转换为 16 进制以下的任何进制
import sys
sys.path.append('.')

from pythonds.basic.stack import Stack

def convert(dec_num, base):
    if (not isinstance(base, int)) or (not isinstance(dec_num, int)) or base <2 or base > 16:
        print('Invaild Input')
        return
    
    char = '0123456789ABCDEF'
    output_s = Stack()
    while dec_num > 0:
        rem = dec_num % base
        output_s.push(rem)
        dec_num = dec_num // base
    
    digit = ''
    while not output_s.isEmpty():
        digit += char[output_s.pop()]
    
    return digit

# 递归实现
def convertR(num, base):
    char = '0123456789ABCDEF'
    if num < base:
        return char[num]
    else:
        rem = num % base
        num = num // base
        return convertR(num, base) + char[rem]

if __name__ == '__main__':
    print(convert(3901, 16))
    print(convertR(3901, 16))