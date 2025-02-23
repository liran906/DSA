# Maximum Subarray
# https://neetcode.io/problems/maximum-subarray
# m

# sliding window, or two pointers
class Solution:
    def maxSubArray(self, nums):
        res = nums[0]   # result: the max current_sum
        current_sum = 0 # current non-negative sum
        for i in range(len(nums)):
            current_sum += nums[i]
            res = max(current_sum, res)
            if current_sum < 0:
                current_sum = 0
        return res

# Dynamic Programming (Space Optimized)
# check solution 5
class Solution:
    def maxSubArray(self, nums):
        for i in range(1, len(nums)):
            if nums[i-1] > 0:
                nums[i] = nums[i] + nums[i-1]
        return max(nums)