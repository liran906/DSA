# https://leetcode.cn/problems/3sum/
# m

class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        res = []
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            target = -nums[i]
            while l < r:
                if nums[l] + nums[r] > target:
                    r -= 1
                elif nums[l] + nums[r] < target:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    r -= 1
                    l += 1

                    # 注意r和l都要检测是否是相同元素
                    while l < r and  nums[l] == nums[l-1]:
                        l += 1
                    while l < r and  nums[r] == nums[r+1]:
                        r -= 1
        return res

s = Solution()
print(s.threeSum([-1,0,1,2,-1,-4]))