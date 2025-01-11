def convert(num, m, n):
    char = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    num, m, n = str(num), int(m), int(n)

    # 用递归转换为 10 进制时，在 oj 上报 runtimeerror，不明白为啥。
    # def convert_10(num, m): # 先转化为十进制
    #     if len(num) == 1:
    #         return char.index(num)
    #     else:
    #         hightestdigit = char.index(num[0]) * m ** (len(num) - 1)
    #         return convert_10(num[1:], m) + hightestdigit

    # 这个也用递归，但是是从个位数开始
    def convert_10(num, m):
        if len(num) == 1:
            return char.index(num)
        else:
            return convert_10(num[:-1], m) * n + char.index(num[-1])
    
    # 不采用递归的方法
    def convert_10(num, m):
        sum = 0
        for i in range(len(num)):
            n = char.index(num[::-1][i])
            sum += n * (m ** i)
        return sum
    
    def convert_n(num, n): # 十进制转换为 n 进制
        if num < n:
            return char[num]
        else:
            rem = num % n
            num = num // n
            return convert_n(num, n) + char[rem]
    
    return convert_n(convert_10(num, m), n)

m, n = input().split()
num = input()
print(convert(num, m, n))

# print(convert('1ZZZZZ2', 36, 14))