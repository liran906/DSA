# Longest Consecutive Sequence
# https://neetcode.io/problems/longest-consecutive-sequence
# m

# store values in hash table for O(1) look up
# O(n)
class Solution:
    def longestConsecutive(self, nums):
        num_set = set(nums)
        res = 0
        for i in nums:
            if i - 1 not in num_set: # if i - 1 not in nums, then i can be the start
                count = 1
                while i + 1 in num_set:
                    i += 1
                    count += 1
                res = max(res, count)
        return res