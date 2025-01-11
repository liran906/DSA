# OJ 结果不对，但我觉得没问题了。
def findAnagrams(s, p):
    if len(s) < len(p):
        return 'none'
    
    # 初始化频率表
    pd = {_:0 for _ in 'abcdefghijklmnopqrstuvwxyz'}
    for i in p:
        pd[i] += 1
    
    sd = {_:0 for _ in 'abcdefghijklmnopqrstuvwxyz'}
    for i in s[:len(p)]:
        sd[i] += 1
    
    # 检查初始窗口
    out = []
    if sd == pd:
        out.append('0')

    # 滑动窗口
    for i in range(1, len(s) - len(p) + 1):
        prevchar = s[i - 1]
        newchar = s[i + len(p) - 1]
        sd[prevchar] -= 1
        sd[newchar] += 1

        # 判断是否匹配
        if sd == pd:
            out.append(str(i))
    
    # 输出结果
    if out == []:
        return 'none'
    else:
        return ' '.join(sorted(out))

s = input()
p = input()
print(findAnagrams(s, p))

s = 'abababa'
p = 'aba'