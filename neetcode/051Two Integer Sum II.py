# Two Integer Sum II
# https://neetcode.io/problems/two-integer-sum-ii
# m

class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        tsum = numbers[r] + numbers[l]
        while l < r:
            tsum = numbers[r] + numbers[l]
            if tsum > target:
                r -= 1
            elif tsum < target:
                l += 1
            else:
                return [l + 1, r + 1]
        return []