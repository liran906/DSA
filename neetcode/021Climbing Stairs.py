# Climbing Stairs
# https://neetcode.io/problems/climbing-stairs
# e

# Recursion O(2^n), space: O(n)
class Solution:
    def climbStairs(self, n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1) + self.climbStairs(n-2)

# Dynamic Programming (Bottom-Up) time: O(n), space: O(n)
class Solution:
    def __init__(self):
        self.memo = {1:1, 2:2}

    def climbStairs(self, n):
        if n in self.memo:
            return self.memo[n]
        for i in range(3, n + 1):
            self.memo[i] = self.climbStairs(i - 1) + self.climbStairs(i - 2)
        return self.memo[n]

# Math? time: O(n), space: O(1)
class Solution:
    def climbStairs(self, n):
        currentStep = 1
        previousStep = 1
        for i in range(n - 1): # started from n = 1 (instead of 0), so only range to n - 1
            currentStep, previousStep = currentStep + previousStep, currentStep
        return currentStep