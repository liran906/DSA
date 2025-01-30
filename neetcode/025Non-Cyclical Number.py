# Non-Cyclical Number
# https://neetcode.io/problems/non-cyclical-number
# e

# can also use 2-pointer method to optimize space to O(1), but I think this method is better.
class Solution:
    def isHappy(self, n):
        seen = set()
        ss = self.squareSum(n)
        while ss != 1 and ss not in seen:
            seen.add(ss)
            ss = self.squareSum(ss)
        return ss == 1
    
    def squareSum(self, n):
        sum = 0
        for d in str(n):
            sum += int(d) ** 2
        return sum