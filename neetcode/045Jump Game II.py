# Jump Game II
# https://neetcode.io/problems/jump-game-ii
# m

# O(n)
class Solution:
    def jump(self, nums):
        l = r = 0 # left and right index (boundary)
        count = 0 # step count
        while r < len(nums) - 1:
            farthest = 0 # fathest in a step
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i])
            l = r + 1    # next step's left boundary
            r = farthest # next step's right boundary
            count += 1
        return count