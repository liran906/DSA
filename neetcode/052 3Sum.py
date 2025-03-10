# 3Sum
# https://neetcode.io/problems/three-integer-sum
# m

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = set()
        l, m, r = 0, len(nums) - 2, len(nums) - 1

        while l < r - 1 and nums[r] >= 0:
            while l < m:
                if nums[l] + nums[r] + nums[m] > 0:
                    m -= 1
                elif nums[l] + nums[r] + nums[m] < 0:
                    l += 1
                else:
                    res.add((nums[l], nums[m], nums[r]))
                    m -= 1
            r -= 1
            l, m = 0, r - 1
        return [list(i) for i in res]

class Solution:
    def threeSum(self, nums):
        nums.sort()
        res = []

        for i in range(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                if nums[i] + nums[l] + nums[r] > 0:
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    tmp = nums[l]
                    while nums[l] == tmp and l < r:
                        l += 1
        return res

s = Solution()

print(s.threeSum(nums=[-1,0,1,2,-1,-4,-2,-3,3,0,4]))