# Largest Rectangle In Histogram
# https://neetcode.io/problems/largest-rectangle-in-histogram
# h

class Solution:
    def largestRectangleArea(self, heights):
        heights.append(0) # add a 0 to finish all remaining values in stack at the end.
        stack = []
        area = 0
        for i in range(len(heights)):
            index = i
            while stack and stack[-1][1] > heights[i]:
                l, h = stack.pop()
                area = max(area, (i - l) * h)
                index = l
            stack.append((index, heights[i])) # note the index here is l (last popped element's index)
        return area

# not altering the heights list
class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        area = 0

        for i in range(len(heights)):
            index = i
            while stack and stack[-1][1] > heights[i]:
                l, h = stack.pop()
                area = max(area, (i - l) * h)
                index = l
            stack.append((index, heights[i])) # note the index here is l (last popped element's index)
        
        # deal with the remaining values
        for l, h in stack:
            area = max(area, (len(heights) - l) * h)
        return area