# Container With Most Water
# https://neetcode.io/problems/max-water-container
# m

class Solution:
    def maxArea(self, heights):
        l, r = 0, len(heights) - 1
        area = 0
        while l < r:
            c_area = min(heights[l], heights[r]) * (r - l)
            area = max(area, c_area)
            if heights[l] > heights[r]:
                r -= 1
            else:
                l += 1
        return area