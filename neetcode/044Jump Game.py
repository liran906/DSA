# Jump Game
# https://neetcode.io/problems/jump-game
# m

# Dynamic Programming
# O(n^2)
class Solution:
    def canJump(self, nums):
        # turth list, true if the step is reachable
        blst = [True] + [False] * (len(nums) - 1)
        i = 0

        # while (i in nums) and (current was perviously marked as reachable) and (last step not marked reachable)
        while i < len(nums) and blst[i] and not blst[-1]:
            # if max jump lenth > 0
            if nums[i]:
                # for the current step i, mark the j=nums[i] steps ahead true(reachable).
                j = 1
                while i + j < len(nums) and j <= nums[i]:
                    if not blst[i+j]:
                        blst[i+j] = True
                    j += 1
            i += 1
        return blst[-1]

s = Solution()
s.canJump([1,2,0,1,0])

# greedy? check solution 4
# O(n)
class Solution:
    def canJump(self, nums):
        goal = len(nums) - 1
        for i in range(len(nums) - 2, -1, -1):
            # if can reach goal from i, set goal to i
            if i + nums[i] >= goal:
                goal = i
        return goal == 0

# inspired by above.
class Solution:
    def canJump(self, nums):
        # farthert jump
        farthest = i = 0

        # iterate while i does to exceed len(nums) and farthest jump
        while i < len(nums) and i <= farthest:
            farthest = max(farthest, i + nums[i])
            i += 1
        return farthest >= len(nums) - 1