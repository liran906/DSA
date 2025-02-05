# Kth Largest Element in an Array
# https://neetcode.io/problems/kth-largest-element-in-an-array
# m

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        minheap = []
        for i in nums:
            heapq.heappush(minheap, i)
            if len(minheap) > k:
                heapq.heappop(minheap)
        return heapq.heappop(minheap)