# Pow(x, n)
# https://neetcode.io/problems/pow-x-n
# m

class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for i in range(abs(n)):
            res *= x
        if n < 0:
            res = 1 / res
        return res