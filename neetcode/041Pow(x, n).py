# Pow(x, n)
# https://neetcode.io/problems/pow-x-n
# m

# Brute force O(n)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        res = 1
        for i in range(abs(n)):
            res *= x
        if n < 0:
            res = 1 / res
        return res

# O(log n)
class Solution:
    def myPow(self, x: float, n: int):
        if x == 1:
            return 1
        if n == 0:
            return 1
        if n == 1:
            return x
        if n == -1:
            return 1 / x
        
        if n % 2 == 0:
            # compare with self.myPow(x**2, n//2)
            return self.myPow(x, n//2) ** 2
        else:
            return self.myPow(x, n//2) ** 2 * x

# if self.myPow(x**2, n//2), this case will not pass:
s = Solution()
x = 2.0
n = 200000000

print(s.myPow(x, n))