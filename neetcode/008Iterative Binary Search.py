#  Iterative Binary Search
# https://neetcode.io/problems/binary-search
# easy

class Solution:
    def search(self, nums, target):
        if not nums:
            return -1
        
        index = len(nums) // 2
        if nums[index] == target:
            return index
        else:
            if nums[index] > target:
                return self.search(nums[:index], target)
            else:
                result = self.search(nums[index+1:], target)
                return -1 if result == -1 else result + index + 1