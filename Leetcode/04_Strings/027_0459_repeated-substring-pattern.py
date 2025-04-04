# https://leetcode.cn/problems/repeated-substring-pattern/description/
# e

# 把给的字符串*2, 扣除首尾第一个字符如果还包含给的字符串本身，则返回 true
class Solution(object):
    def repeatedSubstringPattern(self, s):
        ns = s + s
        n = len(s)
        for i in range(1, n):
            if s == ns[i:i+n]:
                return True
        return False
    
class Solution(object):
    def repeatedSubstringPattern(self, s):
        return s in (s*2)[1:-1]


# KMP解法，更高效：
class Solution(object):
    def repeatedSubstringPattern(self, s):
        # KMP 算法求出 next
        n = len(s)
        nxt = [0] * n
        i = 0
        for j in range(1, n):
            while s[j] != s[i] and i > 0:
                i = nxt[i-1]
            if s[j] == s[i]:
                i += 1
            nxt[j] = i
        
        # 判断能否整除
        rem = n - nxt[n-1]
        return nxt[n-1] > 0 and n % rem == 0