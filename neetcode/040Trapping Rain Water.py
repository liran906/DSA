# Trapping Rain Water
# https://neetcode.io/problems/trapping-rain-water
# h

# my method: left + right traversal, time = O(n) space = O(1)
class Solution:
    def trap(self, height):
        if len(height) <= 2:
            return 0
        
        vol = 0 # volume

        # from left to right
        t_height = t_vol = 0 # t for temporary
        for pos in range(len(height)):
            if height[pos] >= t_height:
                vol += t_vol
                t_vol = 0
                t_height = height[pos]
            else:
                t_vol += t_height - height[pos]
        
        # from right to left
        t_height = t_vol = 0
        for pos in range(len(height) - 1, -1, -1):
            if height[pos] > t_height: # note that left and right can only have one =
                vol += t_vol
                t_vol = 0
                t_height = height[pos]
            else:
                t_vol += t_height - height[pos]
        
        return vol

# 2 pointers method, see the link. time = O(n) space = O(1)
class Solution:
    def trap(self, height):
        if not height:
            return 0
        
        vol = 0
        l, r = 0, len(height)
        leftMax, rightMax = height[l], height[r]

        while l < r:
            if leftMax <= rightMax:
                l += 1
                leftMax = max(leftMax, height[l])
                vol += leftMax - height[l]
            
            else:
                r -= 1
                rightMax = max(rightMax, height[r])
                vol += rightMax - height[r]
        
        return vol