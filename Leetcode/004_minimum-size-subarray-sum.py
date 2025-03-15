# https://leetcode.cn/problems/
# m

# 滑动窗口
class Solution(object):
    def minSubArrayLen(self, target, nums):
        l = r = csum = 0
        min_len = float('inf')

        while r < len(nums):
            csum += nums[r] # 加上右边界的值

            # 对于每一个右边界，找到最短子集的左边界
            while csum >= target:
                csum -= nums[l]
                min_len = min(min_len, r - l + 1)
                l += 1
            
            r += 1
        
        if min_len == float('inf'):
            return 0
        return min_len