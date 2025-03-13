# binary-search
# https://leetcode.cn/problems/binary-search/submissions/609778718/
# e

class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) - 1
        while l <= r:
            m = (l + r) // 2
            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

class Solution(object):
    def search(self, nums, target):
        l, r = 0, len(nums) # 按照左闭右开原则，r 取 len(nums)
        while l < r: # 左闭右开就不需要或等于了，因为没意义
            m = (l + r) // 2
            if nums[m] > target:
                r = m # 右开所以r=m
            elif nums[m] < target:
                l = m + 1
            else:
                return m
        return -1

# recursion
class Solution(object):
    def search(self, nums, target):
        def _search(nums, target, l, r):
            index = (l + r) // 2
            if nums[index] == target:
                return index
            if l >= r:
                return -1
            if nums[index] > target:
                return _search(nums, target, l, index - 1)
            if nums[index] < target:
                return _search(nums, target, index + 1, r)
        return _search(nums, target, 0, len(nums) - 1)