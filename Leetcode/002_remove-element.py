# https://leetcode.cn/problems/remove-element/
# e

class Solution(object):
    def removeElement(self, nums, val):
        i, r = 0, len(nums)
        while r > i: # i == r 时结束
            if nums[i] == val:
                r -= 1
                while r > i and nums[r] == val: # 右指针如果是 val，正好省的换了，r-=1
                    r -= 1
                nums[i], nums[r] = nums[r], nums[i]
            else:
                i += 1
        return i