# https://leetcode.cn/problems/two-sum/
# e

class Solution(object):
    def twoSum(self, nums, target):
        dct = dict()
        for i in range(len(nums)):
            if target - nums[i] in dct:
                return [i, dct[target-nums[i]]]
            dct[nums[i]] = i
        return []