# https://leetcode.cn/problems/4sum/
# m

class Solution(object):
    def fourSum(self, nums, target):
        nums.sort()
        res = []
        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                jackpot = target - nums[i] - nums[j]
                l, r = j+1, len(nums)-1
                while l < r:
                    _sum = nums[l] + nums[r]
                    if _sum > jackpot:
                        r -= 1
                    elif _sum < jackpot:
                        l += 1
                    else:
                        res.append([nums[i], nums[j], nums[l], nums[r]])
                        l += 1
                        r -= 1
                        while l < r and nums[l] == nums[l-1]:
                            l += 1
                        while l < r and nums[r] == nums[r+1]:
                            r -= 1
        return res