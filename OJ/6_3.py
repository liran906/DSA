# 初始化
s = '17+3*8+11*3-10'
# s = input()
nums = []
num = ''
op = []

# 字符串转换为数字和操作符
for i in range(len(s)):
    if s[i].isnumeric():
        num += s[i]
    else:
        op.append(s[i])
        nums.append(int(num))
        num = ''
else:
    nums.append(int(num))

# 操作符转换为运算
def domath(op, n1, n2):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    elif op == '*':
        return n1 * n2
    elif op == '/':
        return n1 / n2

# 主函数，递归思路
cache = {} # 还是要加缓存机制
def rattle(nlst, olst):
    key = (tuple(nlst), tuple(olst))
    if key in cache:
        return cache[key]

    if len(nlst) == 1:
        return nlst # 确保返回的是 list，对应下面的 extend()
    else:
        result = []
        for i in range(len(olst)): # 区别就是不同运算符的先后计算次序
            n1 = nlst[i]
            n2 = nlst[i + 1]
            op = olst[i]
            newnum = domath(op, n1, n2)
            result.extend(rattle(nlst[:i] + [newnum] + nlst[i + 2:] , olst[:i] + olst[i + 1:] ))
        
        result = set(result)
        cache[key] = result
        return result # 担心影响子函数结果，去重排序放在最后输出时。但为了时间复杂度，又加上了

final = sorted(set(rattle(nums, op)))
format_ = ''.join(str(final).strip('[]').split())
print(format_) # 按题目要求。正常只要输出 final 就行

# 原来是下面这个代码，本来想改一下节省空间复杂度，结果还是没有达到目的。
#     else:
#         result = []
#         for i in range(len(olst)):
#             olst_n, nlst_n = olst[:], nlst[:]
#             n1 = nlst_n.pop(i)
#             n2 = nlst_n.pop(i)
#             op = olst_n.pop(i)
#             nlst_n.insert(i, domath(op, n1, n2))
#             result.extend(rattle(nlst_n, olst_n))