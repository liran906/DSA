# https://leetcode.cn/problems/reverse-string-ii/description/
# e

# 数学方法
class Solution(object):
    def reverseStr(self, s, k):
        res = ''
        n = len(s) // (k * 2)
        if len(s) % (k * 2):
            n += 1
        for i in range(n):
            l = 0 + 2 * k * i
            r = k - 1 + 2 * k * i
            while l < r:
                if r >= len(s):
                    r = len(s) - 1
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
        return ''.join(s)

# 迭代方法
class Solution(object):
    def reverseStr(self, s, k):
        s = list(s)
        n = len(s)
        l, r = 0, k-1
        while l < n:
            oldl, oldr = l, r
            if r >= n:
                r = n - 1
            while l < r:
                s[l], s[r] = s[r], s[l]
                l += 1
                r -= 1
            l = oldl + 2*k
            r = oldr + 2*k
        return ''.join(s)

s = Solution()
print(s.reverseStr("abcd", 2))