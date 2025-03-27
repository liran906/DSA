# https://leetcode.cn/problems/happy-number
# e

class Solution(object):
    def isHappy(self, n):
        seen = set()
        while n != 1:
            n = str(n)
            s = 0
            for d in n:
                s += int(d) ** 2
            if s in seen:
                return False
            else:
                seen.add(s)
                n = s
        return True

# 快慢指针
class Solution(object):
    def isHappy(self, n):
        f = s = n
        while f != 1:
            f = self.get_next(self.get_next(f))
            s = self.get_next(s)
            if s == f and s != 1:
                return False
        return True

    def get_next(self, num):
        s = 0
        num = str(num)
        for d in num:
            s += int(d) ** 2
        return s